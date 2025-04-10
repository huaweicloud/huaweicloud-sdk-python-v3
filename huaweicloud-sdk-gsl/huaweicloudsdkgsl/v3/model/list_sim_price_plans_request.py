# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimPricePlansRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sim_card_id': 'int',
        'iccid': 'str',
        'real_time': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'sim_card_id': 'sim_card_id',
        'iccid': 'iccid',
        'real_time': 'real_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, sim_card_id=None, iccid=None, real_time=None, limit=None, offset=None):
        r"""ListSimPricePlansRequest

        The model defined in huaweicloud sdk

        :param sim_card_id: SIM卡标识，可通过[查询SIM卡列表接口](https://support.huaweicloud.com/api-ocgsl/gsl_07_0008.html)获取
        :type sim_card_id: int
        :param iccid: iccid，传入的SIM卡标识（sim_card_id）为0,则根据iccid进行处理
        :type iccid: str
        :param real_time: 是否查实时流量
        :type real_time: bool
        :param limit: 分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数
        :type limit: int
        :param offset: 分页查询时的页码数，默认值为1，取值范围为1-1000000的整数
        :type offset: int
        """
        
        

        self._sim_card_id = None
        self._iccid = None
        self._real_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.sim_card_id = sim_card_id
        if iccid is not None:
            self.iccid = iccid
        if real_time is not None:
            self.real_time = real_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def sim_card_id(self):
        r"""Gets the sim_card_id of this ListSimPricePlansRequest.

        SIM卡标识，可通过[查询SIM卡列表接口](https://support.huaweicloud.com/api-ocgsl/gsl_07_0008.html)获取

        :return: The sim_card_id of this ListSimPricePlansRequest.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        r"""Sets the sim_card_id of this ListSimPricePlansRequest.

        SIM卡标识，可通过[查询SIM卡列表接口](https://support.huaweicloud.com/api-ocgsl/gsl_07_0008.html)获取

        :param sim_card_id: The sim_card_id of this ListSimPricePlansRequest.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def iccid(self):
        r"""Gets the iccid of this ListSimPricePlansRequest.

        iccid，传入的SIM卡标识（sim_card_id）为0,则根据iccid进行处理

        :return: The iccid of this ListSimPricePlansRequest.
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        r"""Sets the iccid of this ListSimPricePlansRequest.

        iccid，传入的SIM卡标识（sim_card_id）为0,则根据iccid进行处理

        :param iccid: The iccid of this ListSimPricePlansRequest.
        :type iccid: str
        """
        self._iccid = iccid

    @property
    def real_time(self):
        r"""Gets the real_time of this ListSimPricePlansRequest.

        是否查实时流量

        :return: The real_time of this ListSimPricePlansRequest.
        :rtype: bool
        """
        return self._real_time

    @real_time.setter
    def real_time(self, real_time):
        r"""Sets the real_time of this ListSimPricePlansRequest.

        是否查实时流量

        :param real_time: The real_time of this ListSimPricePlansRequest.
        :type real_time: bool
        """
        self._real_time = real_time

    @property
    def limit(self):
        r"""Gets the limit of this ListSimPricePlansRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :return: The limit of this ListSimPricePlansRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSimPricePlansRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :param limit: The limit of this ListSimPricePlansRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSimPricePlansRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :return: The offset of this ListSimPricePlansRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSimPricePlansRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :param offset: The offset of this ListSimPricePlansRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListSimPricePlansRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
