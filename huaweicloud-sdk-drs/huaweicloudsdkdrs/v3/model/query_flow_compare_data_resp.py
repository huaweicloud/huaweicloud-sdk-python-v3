# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryFlowCompareDataResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_record': 'int',
        'create_time': 'str',
        'list': 'list[StructDetailVO]'
    }

    attribute_map = {
        'total_record': 'total_record',
        'create_time': 'create_time',
        'list': 'list'
    }

    def __init__(self, total_record=None, create_time=None, list=None):
        """QueryFlowCompareDataResp

        The model defined in huaweicloud sdk

        :param total_record: 任务总数
        :type total_record: int
        :param create_time: 数据生成时间
        :type create_time: str
        :param list: 对比结果
        :type list: list[:class:`huaweicloudsdkdrs.v3.StructDetailVO`]
        """
        
        

        self._total_record = None
        self._create_time = None
        self._list = None
        self.discriminator = None

        if total_record is not None:
            self.total_record = total_record
        if create_time is not None:
            self.create_time = create_time
        if list is not None:
            self.list = list

    @property
    def total_record(self):
        """Gets the total_record of this QueryFlowCompareDataResp.

        任务总数

        :return: The total_record of this QueryFlowCompareDataResp.
        :rtype: int
        """
        return self._total_record

    @total_record.setter
    def total_record(self, total_record):
        """Sets the total_record of this QueryFlowCompareDataResp.

        任务总数

        :param total_record: The total_record of this QueryFlowCompareDataResp.
        :type total_record: int
        """
        self._total_record = total_record

    @property
    def create_time(self):
        """Gets the create_time of this QueryFlowCompareDataResp.

        数据生成时间

        :return: The create_time of this QueryFlowCompareDataResp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryFlowCompareDataResp.

        数据生成时间

        :param create_time: The create_time of this QueryFlowCompareDataResp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def list(self):
        """Gets the list of this QueryFlowCompareDataResp.

        对比结果

        :return: The list of this QueryFlowCompareDataResp.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.StructDetailVO`]
        """
        return self._list

    @list.setter
    def list(self, list):
        """Sets the list of this QueryFlowCompareDataResp.

        对比结果

        :param list: The list of this QueryFlowCompareDataResp.
        :type list: list[:class:`huaweicloudsdkdrs.v3.StructDetailVO`]
        """
        self._list = list

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
        if not isinstance(other, QueryFlowCompareDataResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
