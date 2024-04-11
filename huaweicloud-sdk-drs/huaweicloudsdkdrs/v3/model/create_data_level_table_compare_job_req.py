# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDataLevelTableCompareJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'start_time': 'str',
        'compare_mode': 'str',
        'compare_object': 'list[CompareObjectInfo]',
        'options': 'dict(str, str)',
        'compare_object_with_token': 'list[CompareObjectInfoWithToken]',
        'compare_task_num': 'int',
        'compare_transformation_infos': 'list[AddDataTransformationReq]',
        'proportion_value': 'float'
    }

    attribute_map = {
        'type': 'type',
        'start_time': 'start_time',
        'compare_mode': 'compare_mode',
        'compare_object': 'compare_object',
        'options': 'options',
        'compare_object_with_token': 'compare_object_with_token',
        'compare_task_num': 'compare_task_num',
        'compare_transformation_infos': 'compare_transformation_infos',
        'proportion_value': 'proportion_value'
    }

    def __init__(self, type=None, start_time=None, compare_mode=None, compare_object=None, options=None, compare_object_with_token=None, compare_task_num=None, compare_transformation_infos=None, proportion_value=None):
        """CreateDataLevelTableCompareJobReq

        The model defined in huaweicloud sdk

        :param type: 对比类型。 - lines：行数对比 - contents：内容对比 - random：抽样对比，当前仅支持gaussdbv5、gaussdbv5-to-postgresql、gaussdbv5ha-to-postgresql链路。
        :type type: str
        :param start_time: 对比任务启动时间，时间戳格式，取值为空代表立即启动。
        :type start_time: str
        :param compare_mode: 数据级对比模式，取值为空时需要在compare_object或者compare_object_with_token传对象信息，quick_comparison-快速对比。 取值：quick_comparison
        :type compare_mode: str
        :param compare_object: 数据级对比的对象。
        :type compare_object: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfo`]
        :param options: 对比配置项，key-value形式。 内容对比支持以下配置项： - 对比方式配置，key：contentCompareType，value：dynamic表示动态对比，static表示静态对比。 - lob字段对比类型配置，key：lobCompare，value：ignore表示忽略，length表示长度对比。  行数对比支持以下配置项： - 对比策略配置，多表归一情况下适用，key：comparePolicy，value：normal表示正常对比，manyToOne表示多对一对比。
        :type options: dict(str, str)
        :param compare_object_with_token: 数据级对比的对象（Cassandra灾备专用，带token信息）。
        :type compare_object_with_token: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfoWithToken`]
        :param compare_task_num: 对比任务线程数量，当前仅cloudDataGuard-cassandra和cloudDataGuard-gausscassandra-to-gausscassandra链路支持。
        :type compare_task_num: int
        :param compare_transformation_infos: 过滤数据信息。
        :type compare_transformation_infos: list[:class:`huaweicloudsdkdrs.v3.AddDataTransformationReq`]
        :param proportion_value: 抽样比例，对比类型为抽样对比时填写。
        :type proportion_value: float
        """
        
        

        self._type = None
        self._start_time = None
        self._compare_mode = None
        self._compare_object = None
        self._options = None
        self._compare_object_with_token = None
        self._compare_task_num = None
        self._compare_transformation_infos = None
        self._proportion_value = None
        self.discriminator = None

        self.type = type
        if start_time is not None:
            self.start_time = start_time
        if compare_mode is not None:
            self.compare_mode = compare_mode
        if compare_object is not None:
            self.compare_object = compare_object
        if options is not None:
            self.options = options
        if compare_object_with_token is not None:
            self.compare_object_with_token = compare_object_with_token
        if compare_task_num is not None:
            self.compare_task_num = compare_task_num
        if compare_transformation_infos is not None:
            self.compare_transformation_infos = compare_transformation_infos
        if proportion_value is not None:
            self.proportion_value = proportion_value

    @property
    def type(self):
        """Gets the type of this CreateDataLevelTableCompareJobReq.

        对比类型。 - lines：行数对比 - contents：内容对比 - random：抽样对比，当前仅支持gaussdbv5、gaussdbv5-to-postgresql、gaussdbv5ha-to-postgresql链路。

        :return: The type of this CreateDataLevelTableCompareJobReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateDataLevelTableCompareJobReq.

        对比类型。 - lines：行数对比 - contents：内容对比 - random：抽样对比，当前仅支持gaussdbv5、gaussdbv5-to-postgresql、gaussdbv5ha-to-postgresql链路。

        :param type: The type of this CreateDataLevelTableCompareJobReq.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        """Gets the start_time of this CreateDataLevelTableCompareJobReq.

        对比任务启动时间，时间戳格式，取值为空代表立即启动。

        :return: The start_time of this CreateDataLevelTableCompareJobReq.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this CreateDataLevelTableCompareJobReq.

        对比任务启动时间，时间戳格式，取值为空代表立即启动。

        :param start_time: The start_time of this CreateDataLevelTableCompareJobReq.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def compare_mode(self):
        """Gets the compare_mode of this CreateDataLevelTableCompareJobReq.

        数据级对比模式，取值为空时需要在compare_object或者compare_object_with_token传对象信息，quick_comparison-快速对比。 取值：quick_comparison

        :return: The compare_mode of this CreateDataLevelTableCompareJobReq.
        :rtype: str
        """
        return self._compare_mode

    @compare_mode.setter
    def compare_mode(self, compare_mode):
        """Sets the compare_mode of this CreateDataLevelTableCompareJobReq.

        数据级对比模式，取值为空时需要在compare_object或者compare_object_with_token传对象信息，quick_comparison-快速对比。 取值：quick_comparison

        :param compare_mode: The compare_mode of this CreateDataLevelTableCompareJobReq.
        :type compare_mode: str
        """
        self._compare_mode = compare_mode

    @property
    def compare_object(self):
        """Gets the compare_object of this CreateDataLevelTableCompareJobReq.

        数据级对比的对象。

        :return: The compare_object of this CreateDataLevelTableCompareJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfo`]
        """
        return self._compare_object

    @compare_object.setter
    def compare_object(self, compare_object):
        """Sets the compare_object of this CreateDataLevelTableCompareJobReq.

        数据级对比的对象。

        :param compare_object: The compare_object of this CreateDataLevelTableCompareJobReq.
        :type compare_object: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfo`]
        """
        self._compare_object = compare_object

    @property
    def options(self):
        """Gets the options of this CreateDataLevelTableCompareJobReq.

        对比配置项，key-value形式。 内容对比支持以下配置项： - 对比方式配置，key：contentCompareType，value：dynamic表示动态对比，static表示静态对比。 - lob字段对比类型配置，key：lobCompare，value：ignore表示忽略，length表示长度对比。  行数对比支持以下配置项： - 对比策略配置，多表归一情况下适用，key：comparePolicy，value：normal表示正常对比，manyToOne表示多对一对比。

        :return: The options of this CreateDataLevelTableCompareJobReq.
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CreateDataLevelTableCompareJobReq.

        对比配置项，key-value形式。 内容对比支持以下配置项： - 对比方式配置，key：contentCompareType，value：dynamic表示动态对比，static表示静态对比。 - lob字段对比类型配置，key：lobCompare，value：ignore表示忽略，length表示长度对比。  行数对比支持以下配置项： - 对比策略配置，多表归一情况下适用，key：comparePolicy，value：normal表示正常对比，manyToOne表示多对一对比。

        :param options: The options of this CreateDataLevelTableCompareJobReq.
        :type options: dict(str, str)
        """
        self._options = options

    @property
    def compare_object_with_token(self):
        """Gets the compare_object_with_token of this CreateDataLevelTableCompareJobReq.

        数据级对比的对象（Cassandra灾备专用，带token信息）。

        :return: The compare_object_with_token of this CreateDataLevelTableCompareJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfoWithToken`]
        """
        return self._compare_object_with_token

    @compare_object_with_token.setter
    def compare_object_with_token(self, compare_object_with_token):
        """Sets the compare_object_with_token of this CreateDataLevelTableCompareJobReq.

        数据级对比的对象（Cassandra灾备专用，带token信息）。

        :param compare_object_with_token: The compare_object_with_token of this CreateDataLevelTableCompareJobReq.
        :type compare_object_with_token: list[:class:`huaweicloudsdkdrs.v3.CompareObjectInfoWithToken`]
        """
        self._compare_object_with_token = compare_object_with_token

    @property
    def compare_task_num(self):
        """Gets the compare_task_num of this CreateDataLevelTableCompareJobReq.

        对比任务线程数量，当前仅cloudDataGuard-cassandra和cloudDataGuard-gausscassandra-to-gausscassandra链路支持。

        :return: The compare_task_num of this CreateDataLevelTableCompareJobReq.
        :rtype: int
        """
        return self._compare_task_num

    @compare_task_num.setter
    def compare_task_num(self, compare_task_num):
        """Sets the compare_task_num of this CreateDataLevelTableCompareJobReq.

        对比任务线程数量，当前仅cloudDataGuard-cassandra和cloudDataGuard-gausscassandra-to-gausscassandra链路支持。

        :param compare_task_num: The compare_task_num of this CreateDataLevelTableCompareJobReq.
        :type compare_task_num: int
        """
        self._compare_task_num = compare_task_num

    @property
    def compare_transformation_infos(self):
        """Gets the compare_transformation_infos of this CreateDataLevelTableCompareJobReq.

        过滤数据信息。

        :return: The compare_transformation_infos of this CreateDataLevelTableCompareJobReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.AddDataTransformationReq`]
        """
        return self._compare_transformation_infos

    @compare_transformation_infos.setter
    def compare_transformation_infos(self, compare_transformation_infos):
        """Sets the compare_transformation_infos of this CreateDataLevelTableCompareJobReq.

        过滤数据信息。

        :param compare_transformation_infos: The compare_transformation_infos of this CreateDataLevelTableCompareJobReq.
        :type compare_transformation_infos: list[:class:`huaweicloudsdkdrs.v3.AddDataTransformationReq`]
        """
        self._compare_transformation_infos = compare_transformation_infos

    @property
    def proportion_value(self):
        """Gets the proportion_value of this CreateDataLevelTableCompareJobReq.

        抽样比例，对比类型为抽样对比时填写。

        :return: The proportion_value of this CreateDataLevelTableCompareJobReq.
        :rtype: float
        """
        return self._proportion_value

    @proportion_value.setter
    def proportion_value(self, proportion_value):
        """Sets the proportion_value of this CreateDataLevelTableCompareJobReq.

        抽样比例，对比类型为抽样对比时填写。

        :param proportion_value: The proportion_value of this CreateDataLevelTableCompareJobReq.
        :type proportion_value: float
        """
        self._proportion_value = proportion_value

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
        if not isinstance(other, CreateDataLevelTableCompareJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
