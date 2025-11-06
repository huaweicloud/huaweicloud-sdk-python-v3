# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowResourceCopiesSummaryRequest:

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
        'resource_type': 'str',
        'copy_type': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'region_id': 'region_id',
        'resource_type': 'resource_type',
        'copy_type': 'copy_type',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, domain_id=None, region_id=None, resource_type=None, copy_type=None, start_time=None, end_time=None):
        r"""ShowResourceCopiesSummaryRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param region_id: 区域ID
        :type region_id: str
        :param resource_type: 资源类型
        :type resource_type: str
        :param copy_type: 副本类型
        :type copy_type: str
        :param start_time: 统计起始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type start_time: str
        :param end_time: 统计截止时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type end_time: str
        """
        
        

        self._domain_id = None
        self._region_id = None
        self._resource_type = None
        self._copy_type = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.domain_id = domain_id
        if region_id is not None:
            self.region_id = region_id
        if resource_type is not None:
            self.resource_type = resource_type
        if copy_type is not None:
            self.copy_type = copy_type
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowResourceCopiesSummaryRequest.

        账号ID

        :return: The domain_id of this ShowResourceCopiesSummaryRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowResourceCopiesSummaryRequest.

        账号ID

        :param domain_id: The domain_id of this ShowResourceCopiesSummaryRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowResourceCopiesSummaryRequest.

        区域ID

        :return: The region_id of this ShowResourceCopiesSummaryRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowResourceCopiesSummaryRequest.

        区域ID

        :param region_id: The region_id of this ShowResourceCopiesSummaryRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ShowResourceCopiesSummaryRequest.

        资源类型

        :return: The resource_type of this ShowResourceCopiesSummaryRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ShowResourceCopiesSummaryRequest.

        资源类型

        :param resource_type: The resource_type of this ShowResourceCopiesSummaryRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def copy_type(self):
        r"""Gets the copy_type of this ShowResourceCopiesSummaryRequest.

        副本类型

        :return: The copy_type of this ShowResourceCopiesSummaryRequest.
        :rtype: str
        """
        return self._copy_type

    @copy_type.setter
    def copy_type(self, copy_type):
        r"""Sets the copy_type of this ShowResourceCopiesSummaryRequest.

        副本类型

        :param copy_type: The copy_type of this ShowResourceCopiesSummaryRequest.
        :type copy_type: str
        """
        self._copy_type = copy_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowResourceCopiesSummaryRequest.

        统计起始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The start_time of this ShowResourceCopiesSummaryRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowResourceCopiesSummaryRequest.

        统计起始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param start_time: The start_time of this ShowResourceCopiesSummaryRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowResourceCopiesSummaryRequest.

        统计截止时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The end_time of this ShowResourceCopiesSummaryRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowResourceCopiesSummaryRequest.

        统计截止时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param end_time: The end_time of this ShowResourceCopiesSummaryRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowResourceCopiesSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
