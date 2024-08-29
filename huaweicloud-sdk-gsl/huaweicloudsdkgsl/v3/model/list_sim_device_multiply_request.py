# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimDeviceMultiplyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cid': 'str',
        'online_carrier': 'int',
        'sim_card_id': 'int',
        'version': 'int',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'cid': 'cid',
        'online_carrier': 'online_carrier',
        'sim_card_id': 'sim_card_id',
        'version': 'version',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, cid=None, online_carrier=None, sim_card_id=None, version=None, limit=None, offset=None):
        """ListSimDeviceMultiplyRequest

        The model defined in huaweicloud sdk

        :param cid: cid
        :type cid: str
        :param online_carrier: 在线运营商标识
        :type online_carrier: int
        :param sim_card_id: sim卡id
        :type sim_card_id: int
        :param version: 三网卡版本信息
        :type version: int
        :param limit: 分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数
        :type limit: int
        :param offset: 分页查询时的页码数，默认值为1，取值范围为1-1000000的整数
        :type offset: int
        """
        
        

        self._cid = None
        self._online_carrier = None
        self._sim_card_id = None
        self._version = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if cid is not None:
            self.cid = cid
        if online_carrier is not None:
            self.online_carrier = online_carrier
        if sim_card_id is not None:
            self.sim_card_id = sim_card_id
        if version is not None:
            self.version = version
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def cid(self):
        """Gets the cid of this ListSimDeviceMultiplyRequest.

        cid

        :return: The cid of this ListSimDeviceMultiplyRequest.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this ListSimDeviceMultiplyRequest.

        cid

        :param cid: The cid of this ListSimDeviceMultiplyRequest.
        :type cid: str
        """
        self._cid = cid

    @property
    def online_carrier(self):
        """Gets the online_carrier of this ListSimDeviceMultiplyRequest.

        在线运营商标识

        :return: The online_carrier of this ListSimDeviceMultiplyRequest.
        :rtype: int
        """
        return self._online_carrier

    @online_carrier.setter
    def online_carrier(self, online_carrier):
        """Sets the online_carrier of this ListSimDeviceMultiplyRequest.

        在线运营商标识

        :param online_carrier: The online_carrier of this ListSimDeviceMultiplyRequest.
        :type online_carrier: int
        """
        self._online_carrier = online_carrier

    @property
    def sim_card_id(self):
        """Gets the sim_card_id of this ListSimDeviceMultiplyRequest.

        sim卡id

        :return: The sim_card_id of this ListSimDeviceMultiplyRequest.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        """Sets the sim_card_id of this ListSimDeviceMultiplyRequest.

        sim卡id

        :param sim_card_id: The sim_card_id of this ListSimDeviceMultiplyRequest.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def version(self):
        """Gets the version of this ListSimDeviceMultiplyRequest.

        三网卡版本信息

        :return: The version of this ListSimDeviceMultiplyRequest.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ListSimDeviceMultiplyRequest.

        三网卡版本信息

        :param version: The version of this ListSimDeviceMultiplyRequest.
        :type version: int
        """
        self._version = version

    @property
    def limit(self):
        """Gets the limit of this ListSimDeviceMultiplyRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :return: The limit of this ListSimDeviceMultiplyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSimDeviceMultiplyRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :param limit: The limit of this ListSimDeviceMultiplyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSimDeviceMultiplyRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :return: The offset of this ListSimDeviceMultiplyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSimDeviceMultiplyRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :param offset: The offset of this ListSimDeviceMultiplyRequest.
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
        if not isinstance(other, ListSimDeviceMultiplyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
