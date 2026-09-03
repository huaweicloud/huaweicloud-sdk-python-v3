# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindingFailedDetail:

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
        'skill_id': 'str',
        'error_code': 'str',
        'error_msg': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'skill_id': 'skill_id',
        'error_code': 'error_code',
        'error_msg': 'error_msg'
    }

    def __init__(self, instance_id=None, skill_id=None, error_code=None, error_msg=None):
        r"""BindingFailedDetail

        The model defined in huaweicloud sdk

        :param instance_id: 实例 ID。
        :type instance_id: str
        :param skill_id: 技能 ID。
        :type skill_id: str
        :param error_code: 错误码，格式 WKS.XXXXXXXX。
        :type error_code: str
        :param error_msg: 错误信息。
        :type error_msg: str
        """
        
        

        self._instance_id = None
        self._skill_id = None
        self._error_code = None
        self._error_msg = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if skill_id is not None:
            self.skill_id = skill_id
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BindingFailedDetail.

        实例 ID。

        :return: The instance_id of this BindingFailedDetail.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BindingFailedDetail.

        实例 ID。

        :param instance_id: The instance_id of this BindingFailedDetail.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def skill_id(self):
        r"""Gets the skill_id of this BindingFailedDetail.

        技能 ID。

        :return: The skill_id of this BindingFailedDetail.
        :rtype: str
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        r"""Sets the skill_id of this BindingFailedDetail.

        技能 ID。

        :param skill_id: The skill_id of this BindingFailedDetail.
        :type skill_id: str
        """
        self._skill_id = skill_id

    @property
    def error_code(self):
        r"""Gets the error_code of this BindingFailedDetail.

        错误码，格式 WKS.XXXXXXXX。

        :return: The error_code of this BindingFailedDetail.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this BindingFailedDetail.

        错误码，格式 WKS.XXXXXXXX。

        :param error_code: The error_code of this BindingFailedDetail.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this BindingFailedDetail.

        错误信息。

        :return: The error_msg of this BindingFailedDetail.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this BindingFailedDetail.

        错误信息。

        :param error_msg: The error_msg of this BindingFailedDetail.
        :type error_msg: str
        """
        self._error_msg = error_msg

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
        if not isinstance(other, BindingFailedDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
