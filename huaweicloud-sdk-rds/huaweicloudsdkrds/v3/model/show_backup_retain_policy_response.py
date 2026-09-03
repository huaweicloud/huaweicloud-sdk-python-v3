# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupRetainPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'name': 'str',
        'engine_name': 'str',
        'engine_version': 'str',
        'instance_delete_time': 'int',
        'auto': 'str',
        'manual': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'name': 'name',
        'engine_name': 'engine_name',
        'engine_version': 'engine_version',
        'instance_delete_time': 'instance_delete_time',
        'auto': 'auto',
        'manual': 'manual'
    }

    def __init__(self, instance_id=None, name=None, engine_name=None, engine_version=None, instance_delete_time=None, auto=None, manual=None):
        r"""ShowBackupRetainPolicyResponse

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例id  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type instance_id: str
        :param name: **参数解释**：  实例名字  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type name: str
        :param engine_name: **参数解释**：  引擎类型  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type engine_name: str
        :param engine_version: **参数解释**：  实例引擎版本  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type engine_version: str
        :param instance_delete_time: **参数解释**：  实例删除时间  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及
        :type instance_delete_time: int
        :param auto: **参数解释**  自动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及  **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及
        :type auto: str
        :param manual: **参数解释**  手动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及  **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及
        :type manual: str
        """
        
        super().__init__()

        self._instance_id = None
        self._name = None
        self._engine_name = None
        self._engine_version = None
        self._instance_delete_time = None
        self._auto = None
        self._manual = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if name is not None:
            self.name = name
        if engine_name is not None:
            self.engine_name = engine_name
        if engine_version is not None:
            self.engine_version = engine_version
        if instance_delete_time is not None:
            self.instance_delete_time = instance_delete_time
        if auto is not None:
            self.auto = auto
        if manual is not None:
            self.manual = manual

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowBackupRetainPolicyResponse.

        **参数解释**：  实例id  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The instance_id of this ShowBackupRetainPolicyResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowBackupRetainPolicyResponse.

        **参数解释**：  实例id  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param instance_id: The instance_id of this ShowBackupRetainPolicyResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this ShowBackupRetainPolicyResponse.

        **参数解释**：  实例名字  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The name of this ShowBackupRetainPolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowBackupRetainPolicyResponse.

        **参数解释**：  实例名字  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param name: The name of this ShowBackupRetainPolicyResponse.
        :type name: str
        """
        self._name = name

    @property
    def engine_name(self):
        r"""Gets the engine_name of this ShowBackupRetainPolicyResponse.

        **参数解释**：  引擎类型  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The engine_name of this ShowBackupRetainPolicyResponse.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this ShowBackupRetainPolicyResponse.

        **参数解释**：  引擎类型  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param engine_name: The engine_name of this ShowBackupRetainPolicyResponse.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def engine_version(self):
        r"""Gets the engine_version of this ShowBackupRetainPolicyResponse.

        **参数解释**：  实例引擎版本  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The engine_version of this ShowBackupRetainPolicyResponse.
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        r"""Sets the engine_version of this ShowBackupRetainPolicyResponse.

        **参数解释**：  实例引擎版本  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param engine_version: The engine_version of this ShowBackupRetainPolicyResponse.
        :type engine_version: str
        """
        self._engine_version = engine_version

    @property
    def instance_delete_time(self):
        r"""Gets the instance_delete_time of this ShowBackupRetainPolicyResponse.

        **参数解释**：  实例删除时间  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :return: The instance_delete_time of this ShowBackupRetainPolicyResponse.
        :rtype: int
        """
        return self._instance_delete_time

    @instance_delete_time.setter
    def instance_delete_time(self, instance_delete_time):
        r"""Sets the instance_delete_time of this ShowBackupRetainPolicyResponse.

        **参数解释**：  实例删除时间  **约束限制**  不涉及  **取值范围**  不涉及  **默认取值**  不涉及

        :param instance_delete_time: The instance_delete_time of this ShowBackupRetainPolicyResponse.
        :type instance_delete_time: int
        """
        self._instance_delete_time = instance_delete_time

    @property
    def auto(self):
        r"""Gets the auto of this ShowBackupRetainPolicyResponse.

        **参数解释**  自动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及  **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及

        :return: The auto of this ShowBackupRetainPolicyResponse.
        :rtype: str
        """
        return self._auto

    @auto.setter
    def auto(self, auto):
        r"""Sets the auto of this ShowBackupRetainPolicyResponse.

        **参数解释**  自动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及  **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及

        :param auto: The auto of this ShowBackupRetainPolicyResponse.
        :type auto: str
        """
        self._auto = auto

    @property
    def manual(self):
        r"""Gets the manual of this ShowBackupRetainPolicyResponse.

        **参数解释**  手动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及  **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及

        :return: The manual of this ShowBackupRetainPolicyResponse.
        :rtype: str
        """
        return self._manual

    @manual.setter
    def manual(self, manual):
        r"""Sets the manual of this ShowBackupRetainPolicyResponse.

        **参数解释**  手动备份保留策略。NONE不保留，LAST保留最后一个，ALL全部保留。  **约束限制**  不涉及  **取值范围**  NONE、LAST、ALL  **默认取值**  不涉及

        :param manual: The manual of this ShowBackupRetainPolicyResponse.
        :type manual: str
        """
        self._manual = manual

    def to_dict(self):
        import warnings
        warnings.warn("ShowBackupRetainPolicyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowBackupRetainPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
