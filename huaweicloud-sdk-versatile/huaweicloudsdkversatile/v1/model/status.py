# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Status:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'int',
        'desc': 'str'
    }

    attribute_map = {
        'code': 'code',
        'desc': 'desc'
    }

    def __init__(self, code=None, desc=None):
        r"""Status

        The model defined in huaweicloud sdk

        :param code: 错误码
        :type code: int
        :param desc: 错误描述信息
        :type desc: str
        """
        
        

        self._code = None
        self._desc = None
        self.discriminator = None

        self.code = code
        self.desc = desc

    @property
    def code(self):
        r"""Gets the code of this Status.

        错误码

        :return: The code of this Status.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this Status.

        错误码

        :param code: The code of this Status.
        :type code: int
        """
        self._code = code

    @property
    def desc(self):
        r"""Gets the desc of this Status.

        错误描述信息

        :return: The desc of this Status.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this Status.

        错误描述信息

        :param desc: The desc of this Status.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, Status):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
