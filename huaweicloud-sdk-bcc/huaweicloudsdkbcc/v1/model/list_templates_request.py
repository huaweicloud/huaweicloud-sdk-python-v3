# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'type': 'type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, domain_id=None, type=None, offset=None, limit=None):
        r"""ListTemplatesRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param type: 模板类型，取值为系统预置或者自定义，取值范围：system,custom
        :type type: str
        :param offset: 偏移量，默认取值0，最大取值100
        :type offset: int
        :param limit: 单次请求的条数，取值范围1到100，默认取值10
        :type limit: int
        """
        
        

        self._domain_id = None
        self._type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.domain_id = domain_id
        if type is not None:
            self.type = type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListTemplatesRequest.

        账号ID

        :return: The domain_id of this ListTemplatesRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListTemplatesRequest.

        账号ID

        :param domain_id: The domain_id of this ListTemplatesRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def type(self):
        r"""Gets the type of this ListTemplatesRequest.

        模板类型，取值为系统预置或者自定义，取值范围：system,custom

        :return: The type of this ListTemplatesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListTemplatesRequest.

        模板类型，取值为系统预置或者自定义，取值范围：system,custom

        :param type: The type of this ListTemplatesRequest.
        :type type: str
        """
        self._type = type

    @property
    def offset(self):
        r"""Gets the offset of this ListTemplatesRequest.

        偏移量，默认取值0，最大取值100

        :return: The offset of this ListTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTemplatesRequest.

        偏移量，默认取值0，最大取值100

        :param offset: The offset of this ListTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTemplatesRequest.

        单次请求的条数，取值范围1到100，默认取值10

        :return: The limit of this ListTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTemplatesRequest.

        单次请求的条数，取值范围1到100，默认取值10

        :param limit: The limit of this ListTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
