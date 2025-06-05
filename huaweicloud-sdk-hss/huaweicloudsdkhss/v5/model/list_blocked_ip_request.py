# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBlockedIpRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'last_days': 'int',
        'host_name': 'str',
        'src_ip': 'str',
        'intercept_status': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'last_days': 'last_days',
        'host_name': 'host_name',
        'src_ip': 'src_ip',
        'intercept_status': 'intercept_status',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, region=None, enterprise_project_id=None, last_days=None, host_name=None, src_ip=None, intercept_status=None, offset=None, limit=None):
        r"""ListBlockedIpRequest

        The model defined in huaweicloud sdk

        :param region: Region ID
        :type region: str
        :param enterprise_project_id: 主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。
        :type enterprise_project_id: str
        :param last_days: 查询时间范围天数，与自定义查询时间begin_time，end_time互斥
        :type last_days: int
        :param host_name: 服务器名称
        :type host_name: str
        :param src_ip: 攻击源IP
        :type src_ip: str
        :param intercept_status: 拦截状态，包含如下:   - intercepted : 已拦截   - canceled : 已解除拦截   - cancelling : 待解除拦截
        :type intercept_status: str
        :param offset: 偏移量：指定返回记录的开始位置
        :type offset: int
        :param limit: 每页显示个数
        :type limit: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._last_days = None
        self._host_name = None
        self._src_ip = None
        self._intercept_status = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if last_days is not None:
            self.last_days = last_days
        if host_name is not None:
            self.host_name = host_name
        if src_ip is not None:
            self.src_ip = src_ip
        if intercept_status is not None:
            self.intercept_status = intercept_status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def region(self):
        r"""Gets the region of this ListBlockedIpRequest.

        Region ID

        :return: The region of this ListBlockedIpRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListBlockedIpRequest.

        Region ID

        :param region: The region of this ListBlockedIpRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListBlockedIpRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :return: The enterprise_project_id of this ListBlockedIpRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListBlockedIpRequest.

        主机所属的企业项目ID。 开通企业项目功能后才需要配置企业项目。 企业项目ID默认取值为“0”，表示默认企业项目。如果需要查询所有企业项目下的主机，请传参“all_granted_eps”。如果您只有某个企业项目的权限，则需要传递该企业项目ID，查询该企业项目下的主机，否则会因权限不足而报错。

        :param enterprise_project_id: The enterprise_project_id of this ListBlockedIpRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def last_days(self):
        r"""Gets the last_days of this ListBlockedIpRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :return: The last_days of this ListBlockedIpRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListBlockedIpRequest.

        查询时间范围天数，与自定义查询时间begin_time，end_time互斥

        :param last_days: The last_days of this ListBlockedIpRequest.
        :type last_days: int
        """
        self._last_days = last_days

    @property
    def host_name(self):
        r"""Gets the host_name of this ListBlockedIpRequest.

        服务器名称

        :return: The host_name of this ListBlockedIpRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListBlockedIpRequest.

        服务器名称

        :param host_name: The host_name of this ListBlockedIpRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def src_ip(self):
        r"""Gets the src_ip of this ListBlockedIpRequest.

        攻击源IP

        :return: The src_ip of this ListBlockedIpRequest.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        r"""Sets the src_ip of this ListBlockedIpRequest.

        攻击源IP

        :param src_ip: The src_ip of this ListBlockedIpRequest.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def intercept_status(self):
        r"""Gets the intercept_status of this ListBlockedIpRequest.

        拦截状态，包含如下:   - intercepted : 已拦截   - canceled : 已解除拦截   - cancelling : 待解除拦截

        :return: The intercept_status of this ListBlockedIpRequest.
        :rtype: str
        """
        return self._intercept_status

    @intercept_status.setter
    def intercept_status(self, intercept_status):
        r"""Sets the intercept_status of this ListBlockedIpRequest.

        拦截状态，包含如下:   - intercepted : 已拦截   - canceled : 已解除拦截   - cancelling : 待解除拦截

        :param intercept_status: The intercept_status of this ListBlockedIpRequest.
        :type intercept_status: str
        """
        self._intercept_status = intercept_status

    @property
    def offset(self):
        r"""Gets the offset of this ListBlockedIpRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListBlockedIpRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBlockedIpRequest.

        偏移量：指定返回记录的开始位置

        :param offset: The offset of this ListBlockedIpRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBlockedIpRequest.

        每页显示个数

        :return: The limit of this ListBlockedIpRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBlockedIpRequest.

        每页显示个数

        :param limit: The limit of this ListBlockedIpRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListBlockedIpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
