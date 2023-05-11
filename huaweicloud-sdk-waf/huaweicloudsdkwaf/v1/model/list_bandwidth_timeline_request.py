# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBandwidthTimelineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        '_from': 'int',
        'to': 'int',
        'hosts': 'str',
        'instances': 'str',
        'group_by': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        '_from': 'from',
        'to': 'to',
        'hosts': 'hosts',
        'instances': 'instances',
        'group_by': 'group_by'
    }

    def __init__(self, enterprise_project_id=None, _from=None, to=None, hosts=None, instances=None, group_by=None):
        """ListBandwidthTimelineRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id
        :type enterprise_project_id: str
        :param _from: 查询的带宽统计数据的起始时间（13位毫秒时间戳），需要和to同时使用
        :type _from: int
        :param to: 查询的带宽统计数据的结束时间（13位毫秒时间戳），需要和from同时使用
        :type to: int
        :param hosts: 域名id，用于查询指定的防护域名在from到to这段时间内的带宽数据。通过查询云模式防护域名列表（ListHost）获取域名id或者通过独享模式域名列表（ListPremiumHost）获取域名id
        :type hosts: str
        :param instances: 引擎实例id，用于查询指定的独享引擎实例所防护的域名在from到to这段时间内的带宽数据。
        :type instances: str
        :param group_by: 展示维度，按天展示时传\&quot;DAY\&quot;；默认不传，按照分钟展示。
        :type group_by: str
        """
        
        

        self._enterprise_project_id = None
        self.__from = None
        self._to = None
        self._hosts = None
        self._instances = None
        self._group_by = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self._from = _from
        self.to = to
        if hosts is not None:
            self.hosts = hosts
        if instances is not None:
            self.instances = instances
        if group_by is not None:
            self.group_by = group_by

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListBandwidthTimelineRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :return: The enterprise_project_id of this ListBandwidthTimelineRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListBandwidthTimelineRequest.

        您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目id

        :param enterprise_project_id: The enterprise_project_id of this ListBandwidthTimelineRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def _from(self):
        """Gets the _from of this ListBandwidthTimelineRequest.

        查询的带宽统计数据的起始时间（13位毫秒时间戳），需要和to同时使用

        :return: The _from of this ListBandwidthTimelineRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ListBandwidthTimelineRequest.

        查询的带宽统计数据的起始时间（13位毫秒时间戳），需要和to同时使用

        :param _from: The _from of this ListBandwidthTimelineRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ListBandwidthTimelineRequest.

        查询的带宽统计数据的结束时间（13位毫秒时间戳），需要和from同时使用

        :return: The to of this ListBandwidthTimelineRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ListBandwidthTimelineRequest.

        查询的带宽统计数据的结束时间（13位毫秒时间戳），需要和from同时使用

        :param to: The to of this ListBandwidthTimelineRequest.
        :type to: int
        """
        self._to = to

    @property
    def hosts(self):
        """Gets the hosts of this ListBandwidthTimelineRequest.

        域名id，用于查询指定的防护域名在from到to这段时间内的带宽数据。通过查询云模式防护域名列表（ListHost）获取域名id或者通过独享模式域名列表（ListPremiumHost）获取域名id

        :return: The hosts of this ListBandwidthTimelineRequest.
        :rtype: str
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ListBandwidthTimelineRequest.

        域名id，用于查询指定的防护域名在from到to这段时间内的带宽数据。通过查询云模式防护域名列表（ListHost）获取域名id或者通过独享模式域名列表（ListPremiumHost）获取域名id

        :param hosts: The hosts of this ListBandwidthTimelineRequest.
        :type hosts: str
        """
        self._hosts = hosts

    @property
    def instances(self):
        """Gets the instances of this ListBandwidthTimelineRequest.

        引擎实例id，用于查询指定的独享引擎实例所防护的域名在from到to这段时间内的带宽数据。

        :return: The instances of this ListBandwidthTimelineRequest.
        :rtype: str
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListBandwidthTimelineRequest.

        引擎实例id，用于查询指定的独享引擎实例所防护的域名在from到to这段时间内的带宽数据。

        :param instances: The instances of this ListBandwidthTimelineRequest.
        :type instances: str
        """
        self._instances = instances

    @property
    def group_by(self):
        """Gets the group_by of this ListBandwidthTimelineRequest.

        展示维度，按天展示时传\"DAY\"；默认不传，按照分钟展示。

        :return: The group_by of this ListBandwidthTimelineRequest.
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ListBandwidthTimelineRequest.

        展示维度，按天展示时传\"DAY\"；默认不传，按照分钟展示。

        :param group_by: The group_by of this ListBandwidthTimelineRequest.
        :type group_by: str
        """
        self._group_by = group_by

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
        if not isinstance(other, ListBandwidthTimelineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
