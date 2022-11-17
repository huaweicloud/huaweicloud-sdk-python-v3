# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDiagnosisTaskBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'str',
        'end_time': 'str',
        'node_ip_list': 'list[str]'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'node_ip_list': 'node_ip_list'
    }

    def __init__(self, begin_time=None, end_time=None, node_ip_list=None):
        """CreateDiagnosisTaskBody

        The model defined in huaweicloud sdk

        :param begin_time: 诊断开始时间。UNIX时间戳，单位毫秒。
        :type begin_time: str
        :param end_time: 诊断结束时间。UNIX时间戳，单位毫秒。
        :type end_time: str
        :param node_ip_list: 诊断节点IP列表。默认诊断所有节点。 非读写分离实例查询方法如下：   - 方法一：参考[查看实例信息](https://support.huaweicloud.com/usermanual-dcs/dcs-ug-0312016.html)。   - 方法二：调用[查询指定实例](https://support.huaweicloud.com/api-dcs/ShowInstance.html)查询。  读写分离实例查询方法：调用[查询分片信息](https://support.huaweicloud.com/api-dcs/ListGroupReplicationInfo.html#ListGroupReplicationInfo__response_InstanceReplicationListInfo)。 
        :type node_ip_list: list[str]
        """
        
        

        self._begin_time = None
        self._end_time = None
        self._node_ip_list = None
        self.discriminator = None

        self.begin_time = begin_time
        self.end_time = end_time
        if node_ip_list is not None:
            self.node_ip_list = node_ip_list

    @property
    def begin_time(self):
        """Gets the begin_time of this CreateDiagnosisTaskBody.

        诊断开始时间。UNIX时间戳，单位毫秒。

        :return: The begin_time of this CreateDiagnosisTaskBody.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this CreateDiagnosisTaskBody.

        诊断开始时间。UNIX时间戳，单位毫秒。

        :param begin_time: The begin_time of this CreateDiagnosisTaskBody.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this CreateDiagnosisTaskBody.

        诊断结束时间。UNIX时间戳，单位毫秒。

        :return: The end_time of this CreateDiagnosisTaskBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this CreateDiagnosisTaskBody.

        诊断结束时间。UNIX时间戳，单位毫秒。

        :param end_time: The end_time of this CreateDiagnosisTaskBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def node_ip_list(self):
        """Gets the node_ip_list of this CreateDiagnosisTaskBody.

        诊断节点IP列表。默认诊断所有节点。 非读写分离实例查询方法如下：   - 方法一：参考[查看实例信息](https://support.huaweicloud.com/usermanual-dcs/dcs-ug-0312016.html)。   - 方法二：调用[查询指定实例](https://support.huaweicloud.com/api-dcs/ShowInstance.html)查询。  读写分离实例查询方法：调用[查询分片信息](https://support.huaweicloud.com/api-dcs/ListGroupReplicationInfo.html#ListGroupReplicationInfo__response_InstanceReplicationListInfo)。 

        :return: The node_ip_list of this CreateDiagnosisTaskBody.
        :rtype: list[str]
        """
        return self._node_ip_list

    @node_ip_list.setter
    def node_ip_list(self, node_ip_list):
        """Sets the node_ip_list of this CreateDiagnosisTaskBody.

        诊断节点IP列表。默认诊断所有节点。 非读写分离实例查询方法如下：   - 方法一：参考[查看实例信息](https://support.huaweicloud.com/usermanual-dcs/dcs-ug-0312016.html)。   - 方法二：调用[查询指定实例](https://support.huaweicloud.com/api-dcs/ShowInstance.html)查询。  读写分离实例查询方法：调用[查询分片信息](https://support.huaweicloud.com/api-dcs/ListGroupReplicationInfo.html#ListGroupReplicationInfo__response_InstanceReplicationListInfo)。 

        :param node_ip_list: The node_ip_list of this CreateDiagnosisTaskBody.
        :type node_ip_list: list[str]
        """
        self._node_ip_list = node_ip_list

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
        if not isinstance(other, CreateDiagnosisTaskBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
