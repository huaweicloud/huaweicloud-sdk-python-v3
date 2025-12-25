# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRelationResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'count': 'int',
        'detail_url': 'str',
        'data': 'list[Data]'
    }

    attribute_map = {
        'type': 'type',
        'count': 'count',
        'detail_url': 'detail_url',
        'data': 'data'
    }

    def __init__(self, type=None, count=None, detail_url=None, data=None):
        r"""DeleteRelationResource

        The model defined in huaweicloud sdk

        :param type: 关联资源类型,DPE,ALERT_RULE,DATAOBJECT
        :type type: str
        :param count: 关联数
        :type count: int
        :param detail_url: 关联资源链接
        :type detail_url: str
        :param data: 关联资源信息
        :type data: list[:class:`huaweicloudsdksecmaster.v1.Data`]
        """
        
        

        self._type = None
        self._count = None
        self._detail_url = None
        self._data = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if count is not None:
            self.count = count
        if detail_url is not None:
            self.detail_url = detail_url
        if data is not None:
            self.data = data

    @property
    def type(self):
        r"""Gets the type of this DeleteRelationResource.

        关联资源类型,DPE,ALERT_RULE,DATAOBJECT

        :return: The type of this DeleteRelationResource.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DeleteRelationResource.

        关联资源类型,DPE,ALERT_RULE,DATAOBJECT

        :param type: The type of this DeleteRelationResource.
        :type type: str
        """
        self._type = type

    @property
    def count(self):
        r"""Gets the count of this DeleteRelationResource.

        关联数

        :return: The count of this DeleteRelationResource.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this DeleteRelationResource.

        关联数

        :param count: The count of this DeleteRelationResource.
        :type count: int
        """
        self._count = count

    @property
    def detail_url(self):
        r"""Gets the detail_url of this DeleteRelationResource.

        关联资源链接

        :return: The detail_url of this DeleteRelationResource.
        :rtype: str
        """
        return self._detail_url

    @detail_url.setter
    def detail_url(self, detail_url):
        r"""Sets the detail_url of this DeleteRelationResource.

        关联资源链接

        :param detail_url: The detail_url of this DeleteRelationResource.
        :type detail_url: str
        """
        self._detail_url = detail_url

    @property
    def data(self):
        r"""Gets the data of this DeleteRelationResource.

        关联资源信息

        :return: The data of this DeleteRelationResource.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.Data`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this DeleteRelationResource.

        关联资源信息

        :param data: The data of this DeleteRelationResource.
        :type data: list[:class:`huaweicloudsdksecmaster.v1.Data`]
        """
        self._data = data

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
        if not isinstance(other, DeleteRelationResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
