# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryOrgVmrResultDTO:

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
        'vmr_id': 'str',
        'vmr_name': 'str',
        'vmr_pkg_name': 'str',
        'vmr_pkg_parties': 'int',
        'max_audience_parties': 'int',
        'member': 'IdMarkDTO',
        'device': 'IdMarkDTO',
        'status': 'int',
        'expire_date': 'int',
        'commercial_max_audience_parties': 'int'
    }

    attribute_map = {
        'id': 'id',
        'vmr_id': 'vmrId',
        'vmr_name': 'vmrName',
        'vmr_pkg_name': 'vmrPkgName',
        'vmr_pkg_parties': 'vmrPkgParties',
        'max_audience_parties': 'maxAudienceParties',
        'member': 'member',
        'device': 'device',
        'status': 'status',
        'expire_date': 'expireDate',
        'commercial_max_audience_parties': 'commercialMaxAudienceParties'
    }

    def __init__(self, id=None, vmr_id=None, vmr_name=None, vmr_pkg_name=None, vmr_pkg_parties=None, max_audience_parties=None, member=None, device=None, status=None, expire_date=None, commercial_max_audience_parties=None):
        """QueryOrgVmrResultDTO

        The model defined in huaweicloud sdk

        :param id: 云会议室的ID。 &gt; 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrID。 
        :type id: str
        :param vmr_id: 云会议室的固定会议ID。 &gt; 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrConferenceID。 
        :type vmr_id: str
        :param vmr_name: 云会议室名称。
        :type vmr_name: str
        :param vmr_pkg_name: 云会议室套餐名称。
        :type vmr_pkg_name: str
        :param vmr_pkg_parties: 云会议室套餐会议并发方数。
        :type vmr_pkg_parties: int
        :param max_audience_parties: 最大观众与会方数（仅网络研讨会有效）。
        :type max_audience_parties: int
        :param member: 
        :type member: :class:`huaweicloudsdkmeeting.v1.IdMarkDTO`
        :param device: 
        :type device: :class:`huaweicloudsdkmeeting.v1.IdMarkDTO`
        :param status: 云会议室状态。 * 0：正常 * 1：冻结 * 2：未分配 
        :type status: int
        :param expire_date: 到期时间的时间戳，单位毫秒。
        :type expire_date: int
        :param commercial_max_audience_parties: 按次资源转商后，商用规格最大观众与会方数（仅网络研讨会有效）。
        :type commercial_max_audience_parties: int
        """
        
        

        self._id = None
        self._vmr_id = None
        self._vmr_name = None
        self._vmr_pkg_name = None
        self._vmr_pkg_parties = None
        self._max_audience_parties = None
        self._member = None
        self._device = None
        self._status = None
        self._expire_date = None
        self._commercial_max_audience_parties = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vmr_id is not None:
            self.vmr_id = vmr_id
        if vmr_name is not None:
            self.vmr_name = vmr_name
        if vmr_pkg_name is not None:
            self.vmr_pkg_name = vmr_pkg_name
        if vmr_pkg_parties is not None:
            self.vmr_pkg_parties = vmr_pkg_parties
        if max_audience_parties is not None:
            self.max_audience_parties = max_audience_parties
        if member is not None:
            self.member = member
        if device is not None:
            self.device = device
        if status is not None:
            self.status = status
        if expire_date is not None:
            self.expire_date = expire_date
        if commercial_max_audience_parties is not None:
            self.commercial_max_audience_parties = commercial_max_audience_parties

    @property
    def id(self):
        """Gets the id of this QueryOrgVmrResultDTO.

        云会议室的ID。 > 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrID。 

        :return: The id of this QueryOrgVmrResultDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryOrgVmrResultDTO.

        云会议室的ID。 > 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrID。 

        :param id: The id of this QueryOrgVmrResultDTO.
        :type id: str
        """
        self._id = id

    @property
    def vmr_id(self):
        """Gets the vmr_id of this QueryOrgVmrResultDTO.

        云会议室的固定会议ID。 > 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrConferenceID。 

        :return: The vmr_id of this QueryOrgVmrResultDTO.
        :rtype: str
        """
        return self._vmr_id

    @vmr_id.setter
    def vmr_id(self, vmr_id):
        """Sets the vmr_id of this QueryOrgVmrResultDTO.

        云会议室的固定会议ID。 > 对应[[创建会议](https://support.huaweicloud.com/api-meeting/meeting_21_0014.html)](tag:hws)[[创建会议](https://support.huaweicloud.com/intl/zh-cn/api-meeting/meeting_21_0014.html)](tag:hk)接口中的vmrConferenceID。 

        :param vmr_id: The vmr_id of this QueryOrgVmrResultDTO.
        :type vmr_id: str
        """
        self._vmr_id = vmr_id

    @property
    def vmr_name(self):
        """Gets the vmr_name of this QueryOrgVmrResultDTO.

        云会议室名称。

        :return: The vmr_name of this QueryOrgVmrResultDTO.
        :rtype: str
        """
        return self._vmr_name

    @vmr_name.setter
    def vmr_name(self, vmr_name):
        """Sets the vmr_name of this QueryOrgVmrResultDTO.

        云会议室名称。

        :param vmr_name: The vmr_name of this QueryOrgVmrResultDTO.
        :type vmr_name: str
        """
        self._vmr_name = vmr_name

    @property
    def vmr_pkg_name(self):
        """Gets the vmr_pkg_name of this QueryOrgVmrResultDTO.

        云会议室套餐名称。

        :return: The vmr_pkg_name of this QueryOrgVmrResultDTO.
        :rtype: str
        """
        return self._vmr_pkg_name

    @vmr_pkg_name.setter
    def vmr_pkg_name(self, vmr_pkg_name):
        """Sets the vmr_pkg_name of this QueryOrgVmrResultDTO.

        云会议室套餐名称。

        :param vmr_pkg_name: The vmr_pkg_name of this QueryOrgVmrResultDTO.
        :type vmr_pkg_name: str
        """
        self._vmr_pkg_name = vmr_pkg_name

    @property
    def vmr_pkg_parties(self):
        """Gets the vmr_pkg_parties of this QueryOrgVmrResultDTO.

        云会议室套餐会议并发方数。

        :return: The vmr_pkg_parties of this QueryOrgVmrResultDTO.
        :rtype: int
        """
        return self._vmr_pkg_parties

    @vmr_pkg_parties.setter
    def vmr_pkg_parties(self, vmr_pkg_parties):
        """Sets the vmr_pkg_parties of this QueryOrgVmrResultDTO.

        云会议室套餐会议并发方数。

        :param vmr_pkg_parties: The vmr_pkg_parties of this QueryOrgVmrResultDTO.
        :type vmr_pkg_parties: int
        """
        self._vmr_pkg_parties = vmr_pkg_parties

    @property
    def max_audience_parties(self):
        """Gets the max_audience_parties of this QueryOrgVmrResultDTO.

        最大观众与会方数（仅网络研讨会有效）。

        :return: The max_audience_parties of this QueryOrgVmrResultDTO.
        :rtype: int
        """
        return self._max_audience_parties

    @max_audience_parties.setter
    def max_audience_parties(self, max_audience_parties):
        """Sets the max_audience_parties of this QueryOrgVmrResultDTO.

        最大观众与会方数（仅网络研讨会有效）。

        :param max_audience_parties: The max_audience_parties of this QueryOrgVmrResultDTO.
        :type max_audience_parties: int
        """
        self._max_audience_parties = max_audience_parties

    @property
    def member(self):
        """Gets the member of this QueryOrgVmrResultDTO.

        :return: The member of this QueryOrgVmrResultDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.IdMarkDTO`
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this QueryOrgVmrResultDTO.

        :param member: The member of this QueryOrgVmrResultDTO.
        :type member: :class:`huaweicloudsdkmeeting.v1.IdMarkDTO`
        """
        self._member = member

    @property
    def device(self):
        """Gets the device of this QueryOrgVmrResultDTO.

        :return: The device of this QueryOrgVmrResultDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.IdMarkDTO`
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this QueryOrgVmrResultDTO.

        :param device: The device of this QueryOrgVmrResultDTO.
        :type device: :class:`huaweicloudsdkmeeting.v1.IdMarkDTO`
        """
        self._device = device

    @property
    def status(self):
        """Gets the status of this QueryOrgVmrResultDTO.

        云会议室状态。 * 0：正常 * 1：冻结 * 2：未分配 

        :return: The status of this QueryOrgVmrResultDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QueryOrgVmrResultDTO.

        云会议室状态。 * 0：正常 * 1：冻结 * 2：未分配 

        :param status: The status of this QueryOrgVmrResultDTO.
        :type status: int
        """
        self._status = status

    @property
    def expire_date(self):
        """Gets the expire_date of this QueryOrgVmrResultDTO.

        到期时间的时间戳，单位毫秒。

        :return: The expire_date of this QueryOrgVmrResultDTO.
        :rtype: int
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this QueryOrgVmrResultDTO.

        到期时间的时间戳，单位毫秒。

        :param expire_date: The expire_date of this QueryOrgVmrResultDTO.
        :type expire_date: int
        """
        self._expire_date = expire_date

    @property
    def commercial_max_audience_parties(self):
        """Gets the commercial_max_audience_parties of this QueryOrgVmrResultDTO.

        按次资源转商后，商用规格最大观众与会方数（仅网络研讨会有效）。

        :return: The commercial_max_audience_parties of this QueryOrgVmrResultDTO.
        :rtype: int
        """
        return self._commercial_max_audience_parties

    @commercial_max_audience_parties.setter
    def commercial_max_audience_parties(self, commercial_max_audience_parties):
        """Sets the commercial_max_audience_parties of this QueryOrgVmrResultDTO.

        按次资源转商后，商用规格最大观众与会方数（仅网络研讨会有效）。

        :param commercial_max_audience_parties: The commercial_max_audience_parties of this QueryOrgVmrResultDTO.
        :type commercial_max_audience_parties: int
        """
        self._commercial_max_audience_parties = commercial_max_audience_parties

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
        if not isinstance(other, QueryOrgVmrResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
