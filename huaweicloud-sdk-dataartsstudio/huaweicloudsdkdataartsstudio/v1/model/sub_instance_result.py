# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubInstanceResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_rule_id': 'str',
        'sub_instance_instance_id': 'str',
        'abnormal_table_status': 'str',
        'results': 'list[object]'
    }

    attribute_map = {
        'sub_rule_id': 'sub_rule_id',
        'sub_instance_instance_id': 'sub_instance_instance_id',
        'abnormal_table_status': 'abnormal_table_status',
        'results': 'results'
    }

    def __init__(self, sub_rule_id=None, sub_instance_instance_id=None, abnormal_table_status=None, results=None):
        r"""SubInstanceResult

        The model defined in huaweicloud sdk

        :param sub_rule_id: 子规则ID
        :type sub_rule_id: str
        :param sub_instance_instance_id: 子规则实例ID
        :type sub_instance_instance_id: str
        :param abnormal_table_status: 异常表任务状态 UNSUPPORTED:不支持异常表,READY：准备中,RUNNING：运行中,FAILED：失败,SUCCESS：成功
        :type abnormal_table_status: str
        :param results: 结果集
        :type results: list[object]
        """
        
        

        self._sub_rule_id = None
        self._sub_instance_instance_id = None
        self._abnormal_table_status = None
        self._results = None
        self.discriminator = None

        if sub_rule_id is not None:
            self.sub_rule_id = sub_rule_id
        if sub_instance_instance_id is not None:
            self.sub_instance_instance_id = sub_instance_instance_id
        if abnormal_table_status is not None:
            self.abnormal_table_status = abnormal_table_status
        if results is not None:
            self.results = results

    @property
    def sub_rule_id(self):
        r"""Gets the sub_rule_id of this SubInstanceResult.

        子规则ID

        :return: The sub_rule_id of this SubInstanceResult.
        :rtype: str
        """
        return self._sub_rule_id

    @sub_rule_id.setter
    def sub_rule_id(self, sub_rule_id):
        r"""Sets the sub_rule_id of this SubInstanceResult.

        子规则ID

        :param sub_rule_id: The sub_rule_id of this SubInstanceResult.
        :type sub_rule_id: str
        """
        self._sub_rule_id = sub_rule_id

    @property
    def sub_instance_instance_id(self):
        r"""Gets the sub_instance_instance_id of this SubInstanceResult.

        子规则实例ID

        :return: The sub_instance_instance_id of this SubInstanceResult.
        :rtype: str
        """
        return self._sub_instance_instance_id

    @sub_instance_instance_id.setter
    def sub_instance_instance_id(self, sub_instance_instance_id):
        r"""Sets the sub_instance_instance_id of this SubInstanceResult.

        子规则实例ID

        :param sub_instance_instance_id: The sub_instance_instance_id of this SubInstanceResult.
        :type sub_instance_instance_id: str
        """
        self._sub_instance_instance_id = sub_instance_instance_id

    @property
    def abnormal_table_status(self):
        r"""Gets the abnormal_table_status of this SubInstanceResult.

        异常表任务状态 UNSUPPORTED:不支持异常表,READY：准备中,RUNNING：运行中,FAILED：失败,SUCCESS：成功

        :return: The abnormal_table_status of this SubInstanceResult.
        :rtype: str
        """
        return self._abnormal_table_status

    @abnormal_table_status.setter
    def abnormal_table_status(self, abnormal_table_status):
        r"""Sets the abnormal_table_status of this SubInstanceResult.

        异常表任务状态 UNSUPPORTED:不支持异常表,READY：准备中,RUNNING：运行中,FAILED：失败,SUCCESS：成功

        :param abnormal_table_status: The abnormal_table_status of this SubInstanceResult.
        :type abnormal_table_status: str
        """
        self._abnormal_table_status = abnormal_table_status

    @property
    def results(self):
        r"""Gets the results of this SubInstanceResult.

        结果集

        :return: The results of this SubInstanceResult.
        :rtype: list[object]
        """
        return self._results

    @results.setter
    def results(self, results):
        r"""Sets the results of this SubInstanceResult.

        结果集

        :param results: The results of this SubInstanceResult.
        :type results: list[object]
        """
        self._results = results

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
        if not isinstance(other, SubInstanceResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
