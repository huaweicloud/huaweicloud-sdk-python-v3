# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompareUserInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'src_user_name': 'str',
        'tar_user_name': 'str',
        'src_privileges': 'str',
        'tar_privileges': 'str',
        'is_target_existed': 'bool',
        'compare_result': 'int',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'src_user_name': 'src_user_name',
        'tar_user_name': 'tar_user_name',
        'src_privileges': 'src_privileges',
        'tar_privileges': 'tar_privileges',
        'is_target_existed': 'is_target_existed',
        'compare_result': 'compare_result',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, src_user_name=None, tar_user_name=None, src_privileges=None, tar_privileges=None, is_target_existed=None, compare_result=None, created_at=None, updated_at=None):
        r"""CompareUserInfo

        The model defined in huaweicloud sdk

        :param id: id
        :type id: str
        :param src_user_name: 源数据库账号名称
        :type src_user_name: str
        :param tar_user_name: 目标数据库账号名称
        :type tar_user_name: str
        :param src_privileges: 源数据库账号权限
        :type src_privileges: str
        :param tar_privileges: 目标数据库账号权限
        :type tar_privileges: str
        :param is_target_existed: 目标端是否存在，取值： - false：不存在 - true：存在
        :type is_target_existed: bool
        :param compare_result: 对比结果，取值： - INCONSISTENT：不一致 - UNABLE_TO_COMPARE：无法比对 - CONSISTENT：一致 - TARGET_SCHEMA_NOT_EXIST：目标库不存在 - COMPARE_FAILED：比对失败 - COMPARING：比对中 - WAITING_COMPARE：等待比对 - UNKNOWN：未知错误
        :type compare_result: int
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        """
        
        

        self._id = None
        self._src_user_name = None
        self._tar_user_name = None
        self._src_privileges = None
        self._tar_privileges = None
        self._is_target_existed = None
        self._compare_result = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        self.id = id
        self.src_user_name = src_user_name
        self.tar_user_name = tar_user_name
        self.src_privileges = src_privileges
        self.tar_privileges = tar_privileges
        self.is_target_existed = is_target_existed
        self.compare_result = compare_result
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this CompareUserInfo.

        id

        :return: The id of this CompareUserInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CompareUserInfo.

        id

        :param id: The id of this CompareUserInfo.
        :type id: str
        """
        self._id = id

    @property
    def src_user_name(self):
        r"""Gets the src_user_name of this CompareUserInfo.

        源数据库账号名称

        :return: The src_user_name of this CompareUserInfo.
        :rtype: str
        """
        return self._src_user_name

    @src_user_name.setter
    def src_user_name(self, src_user_name):
        r"""Sets the src_user_name of this CompareUserInfo.

        源数据库账号名称

        :param src_user_name: The src_user_name of this CompareUserInfo.
        :type src_user_name: str
        """
        self._src_user_name = src_user_name

    @property
    def tar_user_name(self):
        r"""Gets the tar_user_name of this CompareUserInfo.

        目标数据库账号名称

        :return: The tar_user_name of this CompareUserInfo.
        :rtype: str
        """
        return self._tar_user_name

    @tar_user_name.setter
    def tar_user_name(self, tar_user_name):
        r"""Sets the tar_user_name of this CompareUserInfo.

        目标数据库账号名称

        :param tar_user_name: The tar_user_name of this CompareUserInfo.
        :type tar_user_name: str
        """
        self._tar_user_name = tar_user_name

    @property
    def src_privileges(self):
        r"""Gets the src_privileges of this CompareUserInfo.

        源数据库账号权限

        :return: The src_privileges of this CompareUserInfo.
        :rtype: str
        """
        return self._src_privileges

    @src_privileges.setter
    def src_privileges(self, src_privileges):
        r"""Sets the src_privileges of this CompareUserInfo.

        源数据库账号权限

        :param src_privileges: The src_privileges of this CompareUserInfo.
        :type src_privileges: str
        """
        self._src_privileges = src_privileges

    @property
    def tar_privileges(self):
        r"""Gets the tar_privileges of this CompareUserInfo.

        目标数据库账号权限

        :return: The tar_privileges of this CompareUserInfo.
        :rtype: str
        """
        return self._tar_privileges

    @tar_privileges.setter
    def tar_privileges(self, tar_privileges):
        r"""Sets the tar_privileges of this CompareUserInfo.

        目标数据库账号权限

        :param tar_privileges: The tar_privileges of this CompareUserInfo.
        :type tar_privileges: str
        """
        self._tar_privileges = tar_privileges

    @property
    def is_target_existed(self):
        r"""Gets the is_target_existed of this CompareUserInfo.

        目标端是否存在，取值： - false：不存在 - true：存在

        :return: The is_target_existed of this CompareUserInfo.
        :rtype: bool
        """
        return self._is_target_existed

    @is_target_existed.setter
    def is_target_existed(self, is_target_existed):
        r"""Sets the is_target_existed of this CompareUserInfo.

        目标端是否存在，取值： - false：不存在 - true：存在

        :param is_target_existed: The is_target_existed of this CompareUserInfo.
        :type is_target_existed: bool
        """
        self._is_target_existed = is_target_existed

    @property
    def compare_result(self):
        r"""Gets the compare_result of this CompareUserInfo.

        对比结果，取值： - INCONSISTENT：不一致 - UNABLE_TO_COMPARE：无法比对 - CONSISTENT：一致 - TARGET_SCHEMA_NOT_EXIST：目标库不存在 - COMPARE_FAILED：比对失败 - COMPARING：比对中 - WAITING_COMPARE：等待比对 - UNKNOWN：未知错误

        :return: The compare_result of this CompareUserInfo.
        :rtype: int
        """
        return self._compare_result

    @compare_result.setter
    def compare_result(self, compare_result):
        r"""Sets the compare_result of this CompareUserInfo.

        对比结果，取值： - INCONSISTENT：不一致 - UNABLE_TO_COMPARE：无法比对 - CONSISTENT：一致 - TARGET_SCHEMA_NOT_EXIST：目标库不存在 - COMPARE_FAILED：比对失败 - COMPARING：比对中 - WAITING_COMPARE：等待比对 - UNKNOWN：未知错误

        :param compare_result: The compare_result of this CompareUserInfo.
        :type compare_result: int
        """
        self._compare_result = compare_result

    @property
    def created_at(self):
        r"""Gets the created_at of this CompareUserInfo.

        创建时间

        :return: The created_at of this CompareUserInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CompareUserInfo.

        创建时间

        :param created_at: The created_at of this CompareUserInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CompareUserInfo.

        更新时间

        :return: The updated_at of this CompareUserInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CompareUserInfo.

        更新时间

        :param updated_at: The updated_at of this CompareUserInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CompareUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
