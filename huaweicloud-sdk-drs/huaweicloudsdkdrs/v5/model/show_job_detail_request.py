# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'x_language': 'str',
        'type': 'str',
        'query_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'compare_type': 'str',
        'query_type': 'str',
        'object_type': 'str',
        'compare_task_id': 'str',
        'source_db_name': 'str',
        'target_db_name': 'str',
        'compare_detail_type': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_language': 'X-Language',
        'type': 'type',
        'query_id': 'query_id',
        'offset': 'offset',
        'limit': 'limit',
        'compare_type': 'compare_type',
        'query_type': 'query_type',
        'object_type': 'object_type',
        'compare_task_id': 'compare_task_id',
        'source_db_name': 'source_db_name',
        'target_db_name': 'target_db_name',
        'compare_detail_type': 'compare_detail_type'
    }

    def __init__(self, job_id=None, x_language=None, type=None, query_id=None, offset=None, limit=None, compare_type=None, query_type=None, object_type=None, compare_task_id=None, source_db_name=None, target_db_name=None, compare_detail_type=None):
        """ShowJobDetailRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param type: 任务详情类型。取值： - overview：任务概览信息。 - detail：任务基本信息。 - network：测试连接结果信息，需配合query_id参数一起查询。 - precheck：预检查结果信息，需配合query_id参数一起查询。 - progress：任务进度信息。 - log：任务日志信息，支持分页查询参数offset与limit。 - comapre：查询对比任务。
        :type type: str
        :param query_id: 通过指定Query ID查询任务详情。  说明：部分type类型的任务详情，需要通过触发该操作的请求返回的query_id进行操作结果查询。
        :type query_id: str
        :param offset: 偏移量，表示查询该偏移量后面的记录。  说明：部分type类型的任务详情支持分页查询，可以通过传递该参数进行分页控制。
        :type offset: int
        :param limit: 查询返回记录的数量限制。  说明：部分type类型的任务详情支持分页查询，可以通过传递该参数进行分页控制。
        :type limit: int
        :param compare_type: 对比任务类型 - object_compare：对象对比。 - line_compare：行对比。 - content_compare：内容对比。 - data_compare：数据对比。
        :type compare_type: str
        :param query_type: 查询对比内容。取值： - overview：对比任务概览。 - list：数据对比任务列表。 - detail：对比详情。
        :type query_type: str
        :param object_type: 查询对象对比详情类型。取值： - DB：库级对比详情。 - TABLE：表级对比详情。 - INDEX：索引对比详情。
        :type object_type: str
        :param compare_task_id: 对比任务ID。
        :type compare_task_id: str
        :param source_db_name: 数据对比源库名称。
        :type source_db_name: str
        :param target_db_name: 数据对比目标库名称。
        :type target_db_name: str
        :param compare_detail_type: 对比结果类型。取值： - compare：对比完成。 - uncompare：无法对比。
        :type compare_detail_type: str
        """
        
        

        self._job_id = None
        self._x_language = None
        self._type = None
        self._query_id = None
        self._offset = None
        self._limit = None
        self._compare_type = None
        self._query_type = None
        self._object_type = None
        self._compare_task_id = None
        self._source_db_name = None
        self._target_db_name = None
        self._compare_detail_type = None
        self.discriminator = None

        self.job_id = job_id
        if x_language is not None:
            self.x_language = x_language
        self.type = type
        if query_id is not None:
            self.query_id = query_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if compare_type is not None:
            self.compare_type = compare_type
        if query_type is not None:
            self.query_type = query_type
        if object_type is not None:
            self.object_type = object_type
        if compare_task_id is not None:
            self.compare_task_id = compare_task_id
        if source_db_name is not None:
            self.source_db_name = source_db_name
        if target_db_name is not None:
            self.target_db_name = target_db_name
        if compare_detail_type is not None:
            self.compare_detail_type = compare_detail_type

    @property
    def job_id(self):
        """Gets the job_id of this ShowJobDetailRequest.

        任务ID。

        :return: The job_id of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ShowJobDetailRequest.

        任务ID。

        :param job_id: The job_id of this ShowJobDetailRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_language(self):
        """Gets the x_language of this ShowJobDetailRequest.

        请求语言类型。

        :return: The x_language of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowJobDetailRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowJobDetailRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def type(self):
        """Gets the type of this ShowJobDetailRequest.

        任务详情类型。取值： - overview：任务概览信息。 - detail：任务基本信息。 - network：测试连接结果信息，需配合query_id参数一起查询。 - precheck：预检查结果信息，需配合query_id参数一起查询。 - progress：任务进度信息。 - log：任务日志信息，支持分页查询参数offset与limit。 - comapre：查询对比任务。

        :return: The type of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowJobDetailRequest.

        任务详情类型。取值： - overview：任务概览信息。 - detail：任务基本信息。 - network：测试连接结果信息，需配合query_id参数一起查询。 - precheck：预检查结果信息，需配合query_id参数一起查询。 - progress：任务进度信息。 - log：任务日志信息，支持分页查询参数offset与limit。 - comapre：查询对比任务。

        :param type: The type of this ShowJobDetailRequest.
        :type type: str
        """
        self._type = type

    @property
    def query_id(self):
        """Gets the query_id of this ShowJobDetailRequest.

        通过指定Query ID查询任务详情。  说明：部分type类型的任务详情，需要通过触发该操作的请求返回的query_id进行操作结果查询。

        :return: The query_id of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._query_id

    @query_id.setter
    def query_id(self, query_id):
        """Sets the query_id of this ShowJobDetailRequest.

        通过指定Query ID查询任务详情。  说明：部分type类型的任务详情，需要通过触发该操作的请求返回的query_id进行操作结果查询。

        :param query_id: The query_id of this ShowJobDetailRequest.
        :type query_id: str
        """
        self._query_id = query_id

    @property
    def offset(self):
        """Gets the offset of this ShowJobDetailRequest.

        偏移量，表示查询该偏移量后面的记录。  说明：部分type类型的任务详情支持分页查询，可以通过传递该参数进行分页控制。

        :return: The offset of this ShowJobDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowJobDetailRequest.

        偏移量，表示查询该偏移量后面的记录。  说明：部分type类型的任务详情支持分页查询，可以通过传递该参数进行分页控制。

        :param offset: The offset of this ShowJobDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowJobDetailRequest.

        查询返回记录的数量限制。  说明：部分type类型的任务详情支持分页查询，可以通过传递该参数进行分页控制。

        :return: The limit of this ShowJobDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowJobDetailRequest.

        查询返回记录的数量限制。  说明：部分type类型的任务详情支持分页查询，可以通过传递该参数进行分页控制。

        :param limit: The limit of this ShowJobDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def compare_type(self):
        """Gets the compare_type of this ShowJobDetailRequest.

        对比任务类型 - object_compare：对象对比。 - line_compare：行对比。 - content_compare：内容对比。 - data_compare：数据对比。

        :return: The compare_type of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._compare_type

    @compare_type.setter
    def compare_type(self, compare_type):
        """Sets the compare_type of this ShowJobDetailRequest.

        对比任务类型 - object_compare：对象对比。 - line_compare：行对比。 - content_compare：内容对比。 - data_compare：数据对比。

        :param compare_type: The compare_type of this ShowJobDetailRequest.
        :type compare_type: str
        """
        self._compare_type = compare_type

    @property
    def query_type(self):
        """Gets the query_type of this ShowJobDetailRequest.

        查询对比内容。取值： - overview：对比任务概览。 - list：数据对比任务列表。 - detail：对比详情。

        :return: The query_type of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ShowJobDetailRequest.

        查询对比内容。取值： - overview：对比任务概览。 - list：数据对比任务列表。 - detail：对比详情。

        :param query_type: The query_type of this ShowJobDetailRequest.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def object_type(self):
        """Gets the object_type of this ShowJobDetailRequest.

        查询对象对比详情类型。取值： - DB：库级对比详情。 - TABLE：表级对比详情。 - INDEX：索引对比详情。

        :return: The object_type of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ShowJobDetailRequest.

        查询对象对比详情类型。取值： - DB：库级对比详情。 - TABLE：表级对比详情。 - INDEX：索引对比详情。

        :param object_type: The object_type of this ShowJobDetailRequest.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def compare_task_id(self):
        """Gets the compare_task_id of this ShowJobDetailRequest.

        对比任务ID。

        :return: The compare_task_id of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._compare_task_id

    @compare_task_id.setter
    def compare_task_id(self, compare_task_id):
        """Sets the compare_task_id of this ShowJobDetailRequest.

        对比任务ID。

        :param compare_task_id: The compare_task_id of this ShowJobDetailRequest.
        :type compare_task_id: str
        """
        self._compare_task_id = compare_task_id

    @property
    def source_db_name(self):
        """Gets the source_db_name of this ShowJobDetailRequest.

        数据对比源库名称。

        :return: The source_db_name of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._source_db_name

    @source_db_name.setter
    def source_db_name(self, source_db_name):
        """Sets the source_db_name of this ShowJobDetailRequest.

        数据对比源库名称。

        :param source_db_name: The source_db_name of this ShowJobDetailRequest.
        :type source_db_name: str
        """
        self._source_db_name = source_db_name

    @property
    def target_db_name(self):
        """Gets the target_db_name of this ShowJobDetailRequest.

        数据对比目标库名称。

        :return: The target_db_name of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._target_db_name

    @target_db_name.setter
    def target_db_name(self, target_db_name):
        """Sets the target_db_name of this ShowJobDetailRequest.

        数据对比目标库名称。

        :param target_db_name: The target_db_name of this ShowJobDetailRequest.
        :type target_db_name: str
        """
        self._target_db_name = target_db_name

    @property
    def compare_detail_type(self):
        """Gets the compare_detail_type of this ShowJobDetailRequest.

        对比结果类型。取值： - compare：对比完成。 - uncompare：无法对比。

        :return: The compare_detail_type of this ShowJobDetailRequest.
        :rtype: str
        """
        return self._compare_detail_type

    @compare_detail_type.setter
    def compare_detail_type(self, compare_detail_type):
        """Sets the compare_detail_type of this ShowJobDetailRequest.

        对比结果类型。取值： - compare：对比完成。 - uncompare：无法对比。

        :param compare_detail_type: The compare_detail_type of this ShowJobDetailRequest.
        :type compare_detail_type: str
        """
        self._compare_detail_type = compare_detail_type

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
        if not isinstance(other, ShowJobDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
