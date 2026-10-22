# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApiInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'int',
        'source_id': 'str',
        'source_secret': 'str'
    }

    attribute_map = {
        'status': 'status',
        'source_id': 'source_id',
        'source_secret': 'source_secret'
    }

    def __init__(self, status=None, source_id=None, source_secret=None):
        r"""ApiInfo

        The model defined in huaweicloud sdk

        :param status: API签名状态（0：禁用，1：启用）
        :type status: int
        :param source_id: 访问密钥ID
        :type source_id: str
        :param source_secret: 秘密访问密钥
        :type source_secret: str
        """
        
        

        self._status = None
        self._source_id = None
        self._source_secret = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if source_id is not None:
            self.source_id = source_id
        if source_secret is not None:
            self.source_secret = source_secret

    @property
    def status(self):
        r"""Gets the status of this ApiInfo.

        API签名状态（0：禁用，1：启用）

        :return: The status of this ApiInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApiInfo.

        API签名状态（0：禁用，1：启用）

        :param status: The status of this ApiInfo.
        :type status: int
        """
        self._status = status

    @property
    def source_id(self):
        r"""Gets the source_id of this ApiInfo.

        访问密钥ID

        :return: The source_id of this ApiInfo.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this ApiInfo.

        访问密钥ID

        :param source_id: The source_id of this ApiInfo.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def source_secret(self):
        r"""Gets the source_secret of this ApiInfo.

        秘密访问密钥

        :return: The source_secret of this ApiInfo.
        :rtype: str
        """
        return self._source_secret

    @source_secret.setter
    def source_secret(self, source_secret):
        r"""Sets the source_secret of this ApiInfo.

        秘密访问密钥

        :param source_secret: The source_secret of this ApiInfo.
        :type source_secret: str
        """
        self._source_secret = source_secret

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
        if not isinstance(other, ApiInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
