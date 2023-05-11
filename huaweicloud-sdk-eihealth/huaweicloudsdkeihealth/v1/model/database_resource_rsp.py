# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseResourceRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'resource_id': 'str',
        'spec': 'DatabaseSpecDto',
        'disk': 'DatabaseDiskDto',
        'charge_mode': 'str',
        'period_num': 'int',
        'create_time': 'str',
        'failure_reason': 'str',
        'status': 'DatabaseStatusEnum'
    }

    attribute_map = {
        'id': 'id',
        'resource_id': 'resource_id',
        'spec': 'spec',
        'disk': 'disk',
        'charge_mode': 'charge_mode',
        'period_num': 'period_num',
        'create_time': 'create_time',
        'failure_reason': 'failure_reason',
        'status': 'status'
    }

    def __init__(self, id=None, resource_id=None, spec=None, disk=None, charge_mode=None, period_num=None, create_time=None, failure_reason=None, status=None):
        """DatabaseResourceRsp

        The model defined in huaweicloud sdk

        :param id: 实例ID
        :type id: str
        :param resource_id: 资源ID
        :type resource_id: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkeihealth.v1.DatabaseSpecDto`
        :param disk: 
        :type disk: :class:`huaweicloudsdkeihealth.v1.DatabaseDiskDto`
        :param charge_mode: 计费模式
        :type charge_mode: str
        :param period_num: 购买周期
        :type period_num: int
        :param create_time: 购买时间，UTC时间
        :type create_time: str
        :param failure_reason: 失败原因
        :type failure_reason: str
        :param status: 
        :type status: :class:`huaweicloudsdkeihealth.v1.DatabaseStatusEnum`
        """
        
        

        self._id = None
        self._resource_id = None
        self._spec = None
        self._disk = None
        self._charge_mode = None
        self._period_num = None
        self._create_time = None
        self._failure_reason = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.resource_id = resource_id
        self.spec = spec
        self.disk = disk
        self.charge_mode = charge_mode
        self.period_num = period_num
        self.create_time = create_time
        self.failure_reason = failure_reason
        self.status = status

    @property
    def id(self):
        """Gets the id of this DatabaseResourceRsp.

        实例ID

        :return: The id of this DatabaseResourceRsp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatabaseResourceRsp.

        实例ID

        :param id: The id of this DatabaseResourceRsp.
        :type id: str
        """
        self._id = id

    @property
    def resource_id(self):
        """Gets the resource_id of this DatabaseResourceRsp.

        资源ID

        :return: The resource_id of this DatabaseResourceRsp.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this DatabaseResourceRsp.

        资源ID

        :param resource_id: The resource_id of this DatabaseResourceRsp.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def spec(self):
        """Gets the spec of this DatabaseResourceRsp.

        :return: The spec of this DatabaseResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DatabaseSpecDto`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this DatabaseResourceRsp.

        :param spec: The spec of this DatabaseResourceRsp.
        :type spec: :class:`huaweicloudsdkeihealth.v1.DatabaseSpecDto`
        """
        self._spec = spec

    @property
    def disk(self):
        """Gets the disk of this DatabaseResourceRsp.

        :return: The disk of this DatabaseResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DatabaseDiskDto`
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this DatabaseResourceRsp.

        :param disk: The disk of this DatabaseResourceRsp.
        :type disk: :class:`huaweicloudsdkeihealth.v1.DatabaseDiskDto`
        """
        self._disk = disk

    @property
    def charge_mode(self):
        """Gets the charge_mode of this DatabaseResourceRsp.

        计费模式

        :return: The charge_mode of this DatabaseResourceRsp.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this DatabaseResourceRsp.

        计费模式

        :param charge_mode: The charge_mode of this DatabaseResourceRsp.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def period_num(self):
        """Gets the period_num of this DatabaseResourceRsp.

        购买周期

        :return: The period_num of this DatabaseResourceRsp.
        :rtype: int
        """
        return self._period_num

    @period_num.setter
    def period_num(self, period_num):
        """Sets the period_num of this DatabaseResourceRsp.

        购买周期

        :param period_num: The period_num of this DatabaseResourceRsp.
        :type period_num: int
        """
        self._period_num = period_num

    @property
    def create_time(self):
        """Gets the create_time of this DatabaseResourceRsp.

        购买时间，UTC时间

        :return: The create_time of this DatabaseResourceRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DatabaseResourceRsp.

        购买时间，UTC时间

        :param create_time: The create_time of this DatabaseResourceRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def failure_reason(self):
        """Gets the failure_reason of this DatabaseResourceRsp.

        失败原因

        :return: The failure_reason of this DatabaseResourceRsp.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this DatabaseResourceRsp.

        失败原因

        :param failure_reason: The failure_reason of this DatabaseResourceRsp.
        :type failure_reason: str
        """
        self._failure_reason = failure_reason

    @property
    def status(self):
        """Gets the status of this DatabaseResourceRsp.

        :return: The status of this DatabaseResourceRsp.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DatabaseStatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DatabaseResourceRsp.

        :param status: The status of this DatabaseResourceRsp.
        :type status: :class:`huaweicloudsdkeihealth.v1.DatabaseStatusEnum`
        """
        self._status = status

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
        if not isinstance(other, DatabaseResourceRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
