# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateThirdPartyAssociateVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'title': 'str',
        'url': 'str',
        'id': 'str'
    }

    attribute_map = {
        'title': 'title',
        'url': 'url',
        'id': 'id'
    }

    def __init__(self, title=None, url=None, id=None):
        r"""UpdateThirdPartyAssociateVO

        The model defined in huaweicloud sdk

        :param title: 工作项下关联外部链接的名称。
        :type title: str
        :param url: 工作项下关联外部链接的地址。
        :type url: str
        :param id: 新关联外部链接时会创建一条数据，该数据的唯一标识ID，可以在查询外部链接接口以及关联外部链接接口响应体中找到。
        :type id: str
        """
        
        

        self._title = None
        self._url = None
        self._id = None
        self.discriminator = None

        self.title = title
        self.url = url
        self.id = id

    @property
    def title(self):
        r"""Gets the title of this UpdateThirdPartyAssociateVO.

        工作项下关联外部链接的名称。

        :return: The title of this UpdateThirdPartyAssociateVO.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this UpdateThirdPartyAssociateVO.

        工作项下关联外部链接的名称。

        :param title: The title of this UpdateThirdPartyAssociateVO.
        :type title: str
        """
        self._title = title

    @property
    def url(self):
        r"""Gets the url of this UpdateThirdPartyAssociateVO.

        工作项下关联外部链接的地址。

        :return: The url of this UpdateThirdPartyAssociateVO.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this UpdateThirdPartyAssociateVO.

        工作项下关联外部链接的地址。

        :param url: The url of this UpdateThirdPartyAssociateVO.
        :type url: str
        """
        self._url = url

    @property
    def id(self):
        r"""Gets the id of this UpdateThirdPartyAssociateVO.

        新关联外部链接时会创建一条数据，该数据的唯一标识ID，可以在查询外部链接接口以及关联外部链接接口响应体中找到。

        :return: The id of this UpdateThirdPartyAssociateVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this UpdateThirdPartyAssociateVO.

        新关联外部链接时会创建一条数据，该数据的唯一标识ID，可以在查询外部链接接口以及关联外部链接接口响应体中找到。

        :param id: The id of this UpdateThirdPartyAssociateVO.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, UpdateThirdPartyAssociateVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
