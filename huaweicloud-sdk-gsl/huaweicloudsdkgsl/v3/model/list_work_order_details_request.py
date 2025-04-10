# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkOrderDetailsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'work_order_id': 'int',
        'main_search_key': 'str',
        'limit': 'int',
        'offset': 'int',
        'sim_type': 'int',
        'status': 'int'
    }

    attribute_map = {
        'work_order_id': 'work_order_id',
        'main_search_key': 'main_search_key',
        'limit': 'limit',
        'offset': 'offset',
        'sim_type': 'sim_type',
        'status': 'status'
    }

    def __init__(self, work_order_id=None, main_search_key=None, limit=None, offset=None, sim_type=None, status=None):
        r"""ListWorkOrderDetailsRequest

        The model defined in huaweicloud sdk

        :param work_order_id: 业务受理ID
        :type work_order_id: int
        :param main_search_key: 容器ID
        :type main_search_key: str
        :param limit: 每页的记录数
        :type limit: int
        :param offset: 页码，最小值是1，最大值为1000000。默认值是1
        :type offset: int
        :param sim_type: SIM卡类型:3.实体卡
        :type sim_type: int
        :param status: 业务受理明细状态：1成功、2处理中、3失败
        :type status: int
        """
        
        

        self._work_order_id = None
        self._main_search_key = None
        self._limit = None
        self._offset = None
        self._sim_type = None
        self._status = None
        self.discriminator = None

        self.work_order_id = work_order_id
        if main_search_key is not None:
            self.main_search_key = main_search_key
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sim_type is not None:
            self.sim_type = sim_type
        if status is not None:
            self.status = status

    @property
    def work_order_id(self):
        r"""Gets the work_order_id of this ListWorkOrderDetailsRequest.

        业务受理ID

        :return: The work_order_id of this ListWorkOrderDetailsRequest.
        :rtype: int
        """
        return self._work_order_id

    @work_order_id.setter
    def work_order_id(self, work_order_id):
        r"""Sets the work_order_id of this ListWorkOrderDetailsRequest.

        业务受理ID

        :param work_order_id: The work_order_id of this ListWorkOrderDetailsRequest.
        :type work_order_id: int
        """
        self._work_order_id = work_order_id

    @property
    def main_search_key(self):
        r"""Gets the main_search_key of this ListWorkOrderDetailsRequest.

        容器ID

        :return: The main_search_key of this ListWorkOrderDetailsRequest.
        :rtype: str
        """
        return self._main_search_key

    @main_search_key.setter
    def main_search_key(self, main_search_key):
        r"""Sets the main_search_key of this ListWorkOrderDetailsRequest.

        容器ID

        :param main_search_key: The main_search_key of this ListWorkOrderDetailsRequest.
        :type main_search_key: str
        """
        self._main_search_key = main_search_key

    @property
    def limit(self):
        r"""Gets the limit of this ListWorkOrderDetailsRequest.

        每页的记录数

        :return: The limit of this ListWorkOrderDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWorkOrderDetailsRequest.

        每页的记录数

        :param limit: The limit of this ListWorkOrderDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListWorkOrderDetailsRequest.

        页码，最小值是1，最大值为1000000。默认值是1

        :return: The offset of this ListWorkOrderDetailsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWorkOrderDetailsRequest.

        页码，最小值是1，最大值为1000000。默认值是1

        :param offset: The offset of this ListWorkOrderDetailsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sim_type(self):
        r"""Gets the sim_type of this ListWorkOrderDetailsRequest.

        SIM卡类型:3.实体卡

        :return: The sim_type of this ListWorkOrderDetailsRequest.
        :rtype: int
        """
        return self._sim_type

    @sim_type.setter
    def sim_type(self, sim_type):
        r"""Sets the sim_type of this ListWorkOrderDetailsRequest.

        SIM卡类型:3.实体卡

        :param sim_type: The sim_type of this ListWorkOrderDetailsRequest.
        :type sim_type: int
        """
        self._sim_type = sim_type

    @property
    def status(self):
        r"""Gets the status of this ListWorkOrderDetailsRequest.

        业务受理明细状态：1成功、2处理中、3失败

        :return: The status of this ListWorkOrderDetailsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListWorkOrderDetailsRequest.

        业务受理明细状态：1成功、2处理中、3失败

        :param status: The status of this ListWorkOrderDetailsRequest.
        :type status: int
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
        if not isinstance(other, ListWorkOrderDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
