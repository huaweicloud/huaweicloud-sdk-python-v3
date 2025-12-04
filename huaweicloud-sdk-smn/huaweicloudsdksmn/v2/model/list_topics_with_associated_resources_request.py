# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTopicsWithAssociatedResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'topic_id': 'str',
        'enterprise_project_id': 'str',
        'name': 'str',
        'fuzzy_name': 'str',
        'fuzzy_display_name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'topic_id': 'topic_id',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'fuzzy_name': 'fuzzy_name',
        'fuzzy_display_name': 'fuzzy_display_name'
    }

    def __init__(self, offset=None, limit=None, topic_id=None, enterprise_project_id=None, name=None, fuzzy_name=None, fuzzy_display_name=None):
        r"""ListTopicsWithAssociatedResourcesRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。
        :type offset: int
        :param limit: 查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。
        :type limit: int
        :param topic_id: 检索的主题ID，完全匹配。
        :type topic_id: str
        :param enterprise_project_id: 企业项目id。
        :type enterprise_project_id: str
        :param name: 检索的主题名称，完全匹配。
        :type name: str
        :param fuzzy_name: 检索的主题名称，模糊匹配。
        :type fuzzy_name: str
        :param fuzzy_display_name: 检索的主题显示名。模糊匹配。参数字节长度不能大于192字节。
        :type fuzzy_display_name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._topic_id = None
        self._enterprise_project_id = None
        self._name = None
        self._fuzzy_name = None
        self._fuzzy_display_name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if topic_id is not None:
            self.topic_id = topic_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if name is not None:
            self.name = name
        if fuzzy_name is not None:
            self.fuzzy_name = fuzzy_name
        if fuzzy_display_name is not None:
            self.fuzzy_display_name = fuzzy_display_name

    @property
    def offset(self):
        r"""Gets the offset of this ListTopicsWithAssociatedResourcesRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :return: The offset of this ListTopicsWithAssociatedResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTopicsWithAssociatedResourcesRequest.

        偏移量。  偏移量为一个大于0小于资源总个数的整数，表示查询该偏移量后面的所有的资源，默认值为0。

        :param offset: The offset of this ListTopicsWithAssociatedResourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListTopicsWithAssociatedResourcesRequest.

        查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :return: The limit of this ListTopicsWithAssociatedResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTopicsWithAssociatedResourcesRequest.

        查询的数量限制。  取值范围：1~100，取值一般为10，20，50。功能说明：每页返回的资源个数。默认值为100。

        :param limit: The limit of this ListTopicsWithAssociatedResourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def topic_id(self):
        r"""Gets the topic_id of this ListTopicsWithAssociatedResourcesRequest.

        检索的主题ID，完全匹配。

        :return: The topic_id of this ListTopicsWithAssociatedResourcesRequest.
        :rtype: str
        """
        return self._topic_id

    @topic_id.setter
    def topic_id(self, topic_id):
        r"""Sets the topic_id of this ListTopicsWithAssociatedResourcesRequest.

        检索的主题ID，完全匹配。

        :param topic_id: The topic_id of this ListTopicsWithAssociatedResourcesRequest.
        :type topic_id: str
        """
        self._topic_id = topic_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListTopicsWithAssociatedResourcesRequest.

        企业项目id。

        :return: The enterprise_project_id of this ListTopicsWithAssociatedResourcesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListTopicsWithAssociatedResourcesRequest.

        企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this ListTopicsWithAssociatedResourcesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this ListTopicsWithAssociatedResourcesRequest.

        检索的主题名称，完全匹配。

        :return: The name of this ListTopicsWithAssociatedResourcesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTopicsWithAssociatedResourcesRequest.

        检索的主题名称，完全匹配。

        :param name: The name of this ListTopicsWithAssociatedResourcesRequest.
        :type name: str
        """
        self._name = name

    @property
    def fuzzy_name(self):
        r"""Gets the fuzzy_name of this ListTopicsWithAssociatedResourcesRequest.

        检索的主题名称，模糊匹配。

        :return: The fuzzy_name of this ListTopicsWithAssociatedResourcesRequest.
        :rtype: str
        """
        return self._fuzzy_name

    @fuzzy_name.setter
    def fuzzy_name(self, fuzzy_name):
        r"""Sets the fuzzy_name of this ListTopicsWithAssociatedResourcesRequest.

        检索的主题名称，模糊匹配。

        :param fuzzy_name: The fuzzy_name of this ListTopicsWithAssociatedResourcesRequest.
        :type fuzzy_name: str
        """
        self._fuzzy_name = fuzzy_name

    @property
    def fuzzy_display_name(self):
        r"""Gets the fuzzy_display_name of this ListTopicsWithAssociatedResourcesRequest.

        检索的主题显示名。模糊匹配。参数字节长度不能大于192字节。

        :return: The fuzzy_display_name of this ListTopicsWithAssociatedResourcesRequest.
        :rtype: str
        """
        return self._fuzzy_display_name

    @fuzzy_display_name.setter
    def fuzzy_display_name(self, fuzzy_display_name):
        r"""Sets the fuzzy_display_name of this ListTopicsWithAssociatedResourcesRequest.

        检索的主题显示名。模糊匹配。参数字节长度不能大于192字节。

        :param fuzzy_display_name: The fuzzy_display_name of this ListTopicsWithAssociatedResourcesRequest.
        :type fuzzy_display_name: str
        """
        self._fuzzy_display_name = fuzzy_display_name

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
        if not isinstance(other, ListTopicsWithAssociatedResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
