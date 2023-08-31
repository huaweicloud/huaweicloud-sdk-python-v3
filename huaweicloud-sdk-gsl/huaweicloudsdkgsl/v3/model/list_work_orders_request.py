# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWorkOrdersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'main_search_key': 'str',
        'limit': 'int',
        'offset': 'int',
        'sim_type': 'int',
        'work_order_type': 'int',
        'status': 'int'
    }

    attribute_map = {
        'main_search_key': 'main_search_key',
        'limit': 'limit',
        'offset': 'offset',
        'sim_type': 'sim_type',
        'work_order_type': 'work_order_type',
        'status': 'status'
    }

    def __init__(self, main_search_key=None, limit=None, offset=None, sim_type=None, work_order_type=None, status=None):
        """ListWorkOrdersRequest

        The model defined in huaweicloud sdk

        :param main_search_key: 业务受理ID
        :type main_search_key: str
        :param limit: 分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数
        :type limit: int
        :param offset: 分页查询时的页码数，默认值为1，取值范围为1-1000000的整数
        :type offset: int
        :param sim_type: SIM卡类型:3.实体卡
        :type sim_type: int
        :param work_order_type: 业务受理类型：1.批量激活实体卡 2.批量转移实体卡 3.创建流量池 4.实体卡复机 5.实体卡停机 6.批量启用或复机 7.批量停用或停机 8.批量订购 9.批量退订 10.实体卡激活 11.申请断网 12.达量断网 13.机卡重绑 14.实名制信息清除 15.实体卡限速 16.批量补卡 17.批量机卡重绑 18.重启已废弃后向流量池 19.批量达量断网 20断网恢复 21取消达量断网 22批量取消达量断网 23批量拆机
        :type work_order_type: int
        :param status: 业务受理状态:：1审核中、2已审核、3处理中、4已完成、5已取消、6失败、7 审核不通过
        :type status: int
        """
        
        

        self._main_search_key = None
        self._limit = None
        self._offset = None
        self._sim_type = None
        self._work_order_type = None
        self._status = None
        self.discriminator = None

        if main_search_key is not None:
            self.main_search_key = main_search_key
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sim_type is not None:
            self.sim_type = sim_type
        if work_order_type is not None:
            self.work_order_type = work_order_type
        if status is not None:
            self.status = status

    @property
    def main_search_key(self):
        """Gets the main_search_key of this ListWorkOrdersRequest.

        业务受理ID

        :return: The main_search_key of this ListWorkOrdersRequest.
        :rtype: str
        """
        return self._main_search_key

    @main_search_key.setter
    def main_search_key(self, main_search_key):
        """Sets the main_search_key of this ListWorkOrdersRequest.

        业务受理ID

        :param main_search_key: The main_search_key of this ListWorkOrdersRequest.
        :type main_search_key: str
        """
        self._main_search_key = main_search_key

    @property
    def limit(self):
        """Gets the limit of this ListWorkOrdersRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :return: The limit of this ListWorkOrdersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListWorkOrdersRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :param limit: The limit of this ListWorkOrdersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListWorkOrdersRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :return: The offset of this ListWorkOrdersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListWorkOrdersRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :param offset: The offset of this ListWorkOrdersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sim_type(self):
        """Gets the sim_type of this ListWorkOrdersRequest.

        SIM卡类型:3.实体卡

        :return: The sim_type of this ListWorkOrdersRequest.
        :rtype: int
        """
        return self._sim_type

    @sim_type.setter
    def sim_type(self, sim_type):
        """Sets the sim_type of this ListWorkOrdersRequest.

        SIM卡类型:3.实体卡

        :param sim_type: The sim_type of this ListWorkOrdersRequest.
        :type sim_type: int
        """
        self._sim_type = sim_type

    @property
    def work_order_type(self):
        """Gets the work_order_type of this ListWorkOrdersRequest.

        业务受理类型：1.批量激活实体卡 2.批量转移实体卡 3.创建流量池 4.实体卡复机 5.实体卡停机 6.批量启用或复机 7.批量停用或停机 8.批量订购 9.批量退订 10.实体卡激活 11.申请断网 12.达量断网 13.机卡重绑 14.实名制信息清除 15.实体卡限速 16.批量补卡 17.批量机卡重绑 18.重启已废弃后向流量池 19.批量达量断网 20断网恢复 21取消达量断网 22批量取消达量断网 23批量拆机

        :return: The work_order_type of this ListWorkOrdersRequest.
        :rtype: int
        """
        return self._work_order_type

    @work_order_type.setter
    def work_order_type(self, work_order_type):
        """Sets the work_order_type of this ListWorkOrdersRequest.

        业务受理类型：1.批量激活实体卡 2.批量转移实体卡 3.创建流量池 4.实体卡复机 5.实体卡停机 6.批量启用或复机 7.批量停用或停机 8.批量订购 9.批量退订 10.实体卡激活 11.申请断网 12.达量断网 13.机卡重绑 14.实名制信息清除 15.实体卡限速 16.批量补卡 17.批量机卡重绑 18.重启已废弃后向流量池 19.批量达量断网 20断网恢复 21取消达量断网 22批量取消达量断网 23批量拆机

        :param work_order_type: The work_order_type of this ListWorkOrdersRequest.
        :type work_order_type: int
        """
        self._work_order_type = work_order_type

    @property
    def status(self):
        """Gets the status of this ListWorkOrdersRequest.

        业务受理状态:：1审核中、2已审核、3处理中、4已完成、5已取消、6失败、7 审核不通过

        :return: The status of this ListWorkOrdersRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListWorkOrdersRequest.

        业务受理状态:：1审核中、2已审核、3处理中、4已完成、5已取消、6失败、7 审核不通过

        :param status: The status of this ListWorkOrdersRequest.
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
        if not isinstance(other, ListWorkOrdersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
