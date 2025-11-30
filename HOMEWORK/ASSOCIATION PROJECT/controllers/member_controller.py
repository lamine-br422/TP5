from __future__ import annotations
from typing import List, Dict, Any
from interfaces.storage_interface import StorageInterface
from observers.data_observer import Subject
from factories.member_factory import MemberFactory


class MemberController(Subject):
    """Controller pour gérer les opérations sur les membres (étudiants, professeurs)"""
    
    def __init__(self, storage: StorageInterface) -> None:
        super().__init__()
        self._storage = storage
        
    def get_all_members(self) -> List[Dict[str, Any]]:
        """Récupère tous les membres depuis le storage"""
        return self._storage.load_members()
    
    def get_students(self) -> List[Dict[str, Any]]:
        """Récupère uniquement les étudiants"""
        members = self.get_all_members()
        return [m for m in members if "student_id" in m]
    
    def get_teachers(self) -> List[Dict[str, Any]]:
        """Récupère uniquement les professeurs"""
        members = self.get_all_members()
        return [m for m in members if "teacher_id" in m]
    
    def get_member_by_id(self, member_id: int, member_type: str = "student") -> Dict[str, Any] | None:
        """Récupère un membre par son ID"""
        members = self.get_all_members()
        id_key = f"{member_type}_id" if member_type in ["student", "teacher"] else "id"
        
        for member in members:
            if member.get(id_key) == member_id:
                return member
        return None
    
    def add_member(self, member: Dict[str, Any]) -> None:
        """Ajoute un nouveau membre"""
        members = self.get_all_members()
        members.append(member)
        self._storage.save_members(members)
        member_type = "student" if "student_id" in member else "teacher"
        self.notify(f"member_added_{member_type}", member)
    
    def delete_member(self, member_id: int, member_type: str = "student") -> bool:
        """Supprime un membre par son ID"""
        members = self.get_all_members()
        id_key = f"{member_type}_id" if member_type in ["student", "teacher"] else "id"
        
        original_count = len(members)
        members = [m for m in members if m.get(id_key) != member_id]
        
        if len(members) < original_count:
            self._storage.save_members(members)
            self.notify(f"member_deleted_{member_type}", {"id": member_id})
            return True
        return False
    
    def get_next_student_id(self) -> int:
        """Retourne le prochain ID disponible pour un étudiant"""
        students = self.get_students()
        if not students:
            return 1
        ids = [s.get("student_id", 0) for s in students if s.get("student_id") is not None]
        return max(ids, default=0) + 1
    
    def get_next_teacher_id(self) -> int:
        """Retourne le prochain ID disponible pour un enseignant"""
        teachers = self.get_teachers()
        if not teachers:
            return 1
        ids = [t.get("teacher_id", 0) for t in teachers if t.get("teacher_id") is not None]
        return max(ids, default=0) + 1

    def update_student_group(self, student_id: int, group: int | None) -> bool:
        """Met à jour le champ 'groupe' d'un étudiant et sauvegarde.

        Retourne True si l'étudiant a été trouvé et mis à jour.
        """
        members = self.get_all_members()
        updated = False
        for member in members:
            if member.get("student_id") == student_id:
                member["groupe"] = group
                updated = True
                break
        if updated:
            self._storage.save_members(members)
            self.notify("member_updated", {"student_id": student_id, "group": group})
        return updated

    def create_student(self, **kwargs) -> Dict[str, Any]:
        """Crée un étudiant en utilisant la Factory"""
        return MemberFactory.create_student(**kwargs)

    def create_teacher(self, **kwargs) -> Dict[str, Any]:
        """Crée un professeur en utilisant la Factory"""
        return MemberFactory.create_teacher(**kwargs)

