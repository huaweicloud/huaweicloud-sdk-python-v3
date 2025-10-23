# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceCopiesRequest:

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
        'region_id': 'str',
        'copy_type': 'str',
        'resource_type': 'str',
        'resource_id': 'str',
        'copy_id': 'str',
        'vault_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'copy_type': 'copy_type',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'copy_id': 'copy_id',
        'vault_id': 'vault_id',
        'limit': 'limit',
        'marker': 'marker',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, domain_id=None, region_id=None, copy_type=None, resource_type=None, resource_id=None, copy_id=None, vault_id=None, limit=None, marker=None, start_time=None, end_time=None):
        r"""ListResourceCopiesRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param copy_type: 备份类型:backup-备份, replication-复制
        :type copy_type: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param copy_id: 备份ID
        :type copy_id: str
        :param vault_id: CBR存储库ID
        :type vault_id: str
        :param limit: 返回的最大数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。
        :type marker: str
        :param start_time: 查询开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type start_time: str
        :param end_time: 查询结束时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type end_time: str
        """
        
        

        self._domain_id = None
        self._region_id = None
        self._copy_type = None
        self._resource_type = None
        self._resource_id = None
        self._copy_id = None
        self._vault_id = None
        self._limit = None
        self._marker = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if copy_type is not None:
            self.copy_type = copy_type
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if copy_id is not None:
            self.copy_id = copy_id
        if vault_id is not None:
            self.vault_id = vault_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ListResourceCopiesRequest.

        账号ID

        :return: The domain_id of this ListResourceCopiesRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ListResourceCopiesRequest.

        账号ID

        :param domain_id: The domain_id of this ListResourceCopiesRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ListResourceCopiesRequest.

        区域ID

        :return: The region_id of this ListResourceCopiesRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ListResourceCopiesRequest.

        区域ID

        :param region_id: The region_id of this ListResourceCopiesRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def copy_type(self):
        r"""Gets the copy_type of this ListResourceCopiesRequest.

        备份类型:backup-备份, replication-复制

        :return: The copy_type of this ListResourceCopiesRequest.
        :rtype: str
        """
        return self._copy_type

    @copy_type.setter
    def copy_type(self, copy_type):
        r"""Sets the copy_type of this ListResourceCopiesRequest.

        备份类型:backup-备份, replication-复制

        :param copy_type: The copy_type of this ListResourceCopiesRequest.
        :type copy_type: str
        """
        self._copy_type = copy_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListResourceCopiesRequest.

        资源类型

        :return: The resource_type of this ListResourceCopiesRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListResourceCopiesRequest.

        资源类型

        :param resource_type: The resource_type of this ListResourceCopiesRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ListResourceCopiesRequest.

        资源ID

        :return: The resource_id of this ListResourceCopiesRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ListResourceCopiesRequest.

        资源ID

        :param resource_id: The resource_id of this ListResourceCopiesRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def copy_id(self):
        r"""Gets the copy_id of this ListResourceCopiesRequest.

        备份ID

        :return: The copy_id of this ListResourceCopiesRequest.
        :rtype: str
        """
        return self._copy_id

    @copy_id.setter
    def copy_id(self, copy_id):
        r"""Sets the copy_id of this ListResourceCopiesRequest.

        备份ID

        :param copy_id: The copy_id of this ListResourceCopiesRequest.
        :type copy_id: str
        """
        self._copy_id = copy_id

    @property
    def vault_id(self):
        r"""Gets the vault_id of this ListResourceCopiesRequest.

        CBR存储库ID

        :return: The vault_id of this ListResourceCopiesRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        r"""Sets the vault_id of this ListResourceCopiesRequest.

        CBR存储库ID

        :param vault_id: The vault_id of this ListResourceCopiesRequest.
        :type vault_id: str
        """
        self._vault_id = vault_id

    @property
    def limit(self):
        r"""Gets the limit of this ListResourceCopiesRequest.

        返回的最大数量

        :return: The limit of this ListResourceCopiesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResourceCopiesRequest.

        返回的最大数量

        :param limit: The limit of this ListResourceCopiesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListResourceCopiesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :return: The marker of this ListResourceCopiesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListResourceCopiesRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页。

        :param marker: The marker of this ListResourceCopiesRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def start_time(self):
        r"""Gets the start_time of this ListResourceCopiesRequest.

        查询开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The start_time of this ListResourceCopiesRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListResourceCopiesRequest.

        查询开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param start_time: The start_time of this ListResourceCopiesRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListResourceCopiesRequest.

        查询结束时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The end_time of this ListResourceCopiesRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListResourceCopiesRequest.

        查询结束时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param end_time: The end_time of this ListResourceCopiesRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListResourceCopiesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
