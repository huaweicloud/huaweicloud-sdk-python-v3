# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmSummaryRequest:

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
        'namespace': 'str',
        'status': 'str',
        'region_id': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'namespace': 'namespace',
        'status': 'status',
        'region_id': 'region_id',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, domain_id=None, namespace=None, status=None, region_id=None, start_time=None, end_time=None):
        r"""ShowAlarmSummaryRequest

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param namespace: 告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB
        :type namespace: str
        :param status: 告警状态，取值范围：ok,alarm,invalid
        :type status: str
        :param region_id: RegionID
        :type region_id: str
        :param start_time: 查询范围起始时间，例如：2025-03-20T09:31:45Z。
        :type start_time: str
        :param end_time: 查询范围结束时间，例如：2025-03-21T09:31:45Z。
        :type end_time: str
        """
        
        

        self._domain_id = None
        self._namespace = None
        self._status = None
        self._region_id = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.domain_id = domain_id
        if namespace is not None:
            self.namespace = namespace
        if status is not None:
            self.status = status
        if region_id is not None:
            self.region_id = region_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def domain_id(self):
        r"""Gets the domain_id of this ShowAlarmSummaryRequest.

        账号ID

        :return: The domain_id of this ShowAlarmSummaryRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this ShowAlarmSummaryRequest.

        账号ID

        :param domain_id: The domain_id of this ShowAlarmSummaryRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowAlarmSummaryRequest.

        告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB

        :return: The namespace of this ShowAlarmSummaryRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowAlarmSummaryRequest.

        告警命名空间，取值范围：SYS.CBR,SYS.RDS,SYS.GaussDB

        :param namespace: The namespace of this ShowAlarmSummaryRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def status(self):
        r"""Gets the status of this ShowAlarmSummaryRequest.

        告警状态，取值范围：ok,alarm,invalid

        :return: The status of this ShowAlarmSummaryRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowAlarmSummaryRequest.

        告警状态，取值范围：ok,alarm,invalid

        :param status: The status of this ShowAlarmSummaryRequest.
        :type status: str
        """
        self._status = status

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowAlarmSummaryRequest.

        RegionID

        :return: The region_id of this ShowAlarmSummaryRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowAlarmSummaryRequest.

        RegionID

        :param region_id: The region_id of this ShowAlarmSummaryRequest.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowAlarmSummaryRequest.

        查询范围起始时间，例如：2025-03-20T09:31:45Z。

        :return: The start_time of this ShowAlarmSummaryRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowAlarmSummaryRequest.

        查询范围起始时间，例如：2025-03-20T09:31:45Z。

        :param start_time: The start_time of this ShowAlarmSummaryRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowAlarmSummaryRequest.

        查询范围结束时间，例如：2025-03-21T09:31:45Z。

        :return: The end_time of this ShowAlarmSummaryRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowAlarmSummaryRequest.

        查询范围结束时间，例如：2025-03-21T09:31:45Z。

        :param end_time: The end_time of this ShowAlarmSummaryRequest.
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
        if not isinstance(other, ShowAlarmSummaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
