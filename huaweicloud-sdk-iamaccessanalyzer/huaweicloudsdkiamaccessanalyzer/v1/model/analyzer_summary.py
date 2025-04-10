# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalyzerSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('name')

    openapi_types = {
        'configuration': 'AnalyzerConfiguration',
        'created_at': 'datetime',
        'id': 'str',
        'last_analyzed_resource': 'str',
        'last_resource_analyzed_at': 'datetime',
        'name': 'str',
        'organization_id': 'str',
        'status': 'str',
        'status_reason': 'StatusReason',
        'tags': 'list[Tag]',
        'type': 'AnalyzerType',
        'urn': 'str'
    }

    attribute_map = {
        'configuration': 'configuration',
        'created_at': 'created_at',
        'id': 'id',
        'last_analyzed_resource': 'last_analyzed_resource',
        'last_resource_analyzed_at': 'last_resource_analyzed_at',
        'name': 'name',
        'organization_id': 'organization_id',
        'status': 'status',
        'status_reason': 'status_reason',
        'tags': 'tags',
        'type': 'type',
        'urn': 'urn'
    }

    def __init__(self, configuration=None, created_at=None, id=None, last_analyzed_resource=None, last_resource_analyzed_at=None, name=None, organization_id=None, status=None, status_reason=None, tags=None, type=None, urn=None):
        r"""AnalyzerSummary

        The model defined in huaweicloud sdk

        :param configuration: 
        :type configuration: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerConfiguration`
        :param created_at: 分析器创建的时间。
        :type created_at: datetime
        :param id: 分析器的唯一标识符。
        :type id: str
        :param last_analyzed_resource: 最近分析的资源的唯一资源标识符。
        :type last_analyzed_resource: str
        :param last_resource_analyzed_at: 最近一次分析资源的时间。
        :type last_resource_analyzed_at: datetime
        :param name: 分析器的名称。
        :type name: str
        :param organization_id: 组织ID。
        :type organization_id: str
        :param status: 分析器的状态。
        :type status: str
        :param status_reason: 
        :type status_reason: :class:`huaweicloudsdkiamaccessanalyzer.v1.StatusReason`
        :param tags: 自定义标签列表。
        :type tags: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Tag`]
        :param type: 
        :type type: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerType`
        :param urn: 分析器的唯一资源标识符。
        :type urn: str
        """
        
        

        self._configuration = None
        self._created_at = None
        self._id = None
        self._last_analyzed_resource = None
        self._last_resource_analyzed_at = None
        self._name = None
        self._organization_id = None
        self._status = None
        self._status_reason = None
        self._tags = None
        self._type = None
        self._urn = None
        self.discriminator = None

        if configuration is not None:
            self.configuration = configuration
        self.created_at = created_at
        self.id = id
        if last_analyzed_resource is not None:
            self.last_analyzed_resource = last_analyzed_resource
        if last_resource_analyzed_at is not None:
            self.last_resource_analyzed_at = last_resource_analyzed_at
        self.name = name
        if organization_id is not None:
            self.organization_id = organization_id
        self.status = status
        if status_reason is not None:
            self.status_reason = status_reason
        if tags is not None:
            self.tags = tags
        self.type = type
        self.urn = urn

    @property
    def configuration(self):
        r"""Gets the configuration of this AnalyzerSummary.

        :return: The configuration of this AnalyzerSummary.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerConfiguration`
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        r"""Sets the configuration of this AnalyzerSummary.

        :param configuration: The configuration of this AnalyzerSummary.
        :type configuration: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerConfiguration`
        """
        self._configuration = configuration

    @property
    def created_at(self):
        r"""Gets the created_at of this AnalyzerSummary.

        分析器创建的时间。

        :return: The created_at of this AnalyzerSummary.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this AnalyzerSummary.

        分析器创建的时间。

        :param created_at: The created_at of this AnalyzerSummary.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this AnalyzerSummary.

        分析器的唯一标识符。

        :return: The id of this AnalyzerSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AnalyzerSummary.

        分析器的唯一标识符。

        :param id: The id of this AnalyzerSummary.
        :type id: str
        """
        self._id = id

    @property
    def last_analyzed_resource(self):
        r"""Gets the last_analyzed_resource of this AnalyzerSummary.

        最近分析的资源的唯一资源标识符。

        :return: The last_analyzed_resource of this AnalyzerSummary.
        :rtype: str
        """
        return self._last_analyzed_resource

    @last_analyzed_resource.setter
    def last_analyzed_resource(self, last_analyzed_resource):
        r"""Sets the last_analyzed_resource of this AnalyzerSummary.

        最近分析的资源的唯一资源标识符。

        :param last_analyzed_resource: The last_analyzed_resource of this AnalyzerSummary.
        :type last_analyzed_resource: str
        """
        self._last_analyzed_resource = last_analyzed_resource

    @property
    def last_resource_analyzed_at(self):
        r"""Gets the last_resource_analyzed_at of this AnalyzerSummary.

        最近一次分析资源的时间。

        :return: The last_resource_analyzed_at of this AnalyzerSummary.
        :rtype: datetime
        """
        return self._last_resource_analyzed_at

    @last_resource_analyzed_at.setter
    def last_resource_analyzed_at(self, last_resource_analyzed_at):
        r"""Sets the last_resource_analyzed_at of this AnalyzerSummary.

        最近一次分析资源的时间。

        :param last_resource_analyzed_at: The last_resource_analyzed_at of this AnalyzerSummary.
        :type last_resource_analyzed_at: datetime
        """
        self._last_resource_analyzed_at = last_resource_analyzed_at

    @property
    def name(self):
        r"""Gets the name of this AnalyzerSummary.

        分析器的名称。

        :return: The name of this AnalyzerSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AnalyzerSummary.

        分析器的名称。

        :param name: The name of this AnalyzerSummary.
        :type name: str
        """
        self._name = name

    @property
    def organization_id(self):
        r"""Gets the organization_id of this AnalyzerSummary.

        组织ID。

        :return: The organization_id of this AnalyzerSummary.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this AnalyzerSummary.

        组织ID。

        :param organization_id: The organization_id of this AnalyzerSummary.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def status(self):
        r"""Gets the status of this AnalyzerSummary.

        分析器的状态。

        :return: The status of this AnalyzerSummary.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AnalyzerSummary.

        分析器的状态。

        :param status: The status of this AnalyzerSummary.
        :type status: str
        """
        self._status = status

    @property
    def status_reason(self):
        r"""Gets the status_reason of this AnalyzerSummary.

        :return: The status_reason of this AnalyzerSummary.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.StatusReason`
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        r"""Sets the status_reason of this AnalyzerSummary.

        :param status_reason: The status_reason of this AnalyzerSummary.
        :type status_reason: :class:`huaweicloudsdkiamaccessanalyzer.v1.StatusReason`
        """
        self._status_reason = status_reason

    @property
    def tags(self):
        r"""Gets the tags of this AnalyzerSummary.

        自定义标签列表。

        :return: The tags of this AnalyzerSummary.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this AnalyzerSummary.

        自定义标签列表。

        :param tags: The tags of this AnalyzerSummary.
        :type tags: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.Tag`]
        """
        self._tags = tags

    @property
    def type(self):
        r"""Gets the type of this AnalyzerSummary.

        :return: The type of this AnalyzerSummary.
        :rtype: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AnalyzerSummary.

        :param type: The type of this AnalyzerSummary.
        :type type: :class:`huaweicloudsdkiamaccessanalyzer.v1.AnalyzerType`
        """
        self._type = type

    @property
    def urn(self):
        r"""Gets the urn of this AnalyzerSummary.

        分析器的唯一资源标识符。

        :return: The urn of this AnalyzerSummary.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this AnalyzerSummary.

        分析器的唯一资源标识符。

        :param urn: The urn of this AnalyzerSummary.
        :type urn: str
        """
        self._urn = urn

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AnalyzerSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
