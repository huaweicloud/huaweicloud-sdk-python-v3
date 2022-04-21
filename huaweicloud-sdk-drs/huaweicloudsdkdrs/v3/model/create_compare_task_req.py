# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCompareTaskReq:

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
        'object_level_compare_type': 'str',
        'data_level_compare_info': 'CreateDataLevelCompareReq'
    }

    attribute_map = {
        'job_id': 'job_id',
        'object_level_compare_type': 'object_level_compare_type',
        'data_level_compare_info': 'data_level_compare_info'
    }

    def __init__(self, job_id=None, object_level_compare_type=None, data_level_compare_info=None):
        """CreateCompareTaskReq

        The model defined in huaweicloud sdk

        :param job_id: 任务id。
        :type job_id: str
        :param object_level_compare_type: 对象级对比类型，取值为空代表不创建对象级对比。object_level_compare_type和data_level_compare_info都为空时，只查询已创建的对比任务列表。
        :type object_level_compare_type: str
        :param data_level_compare_info: 
        :type data_level_compare_info: :class:`huaweicloudsdkdrs.v3.CreateDataLevelCompareReq`
        """
        
        

        self._job_id = None
        self._object_level_compare_type = None
        self._data_level_compare_info = None
        self.discriminator = None

        self.job_id = job_id
        if object_level_compare_type is not None:
            self.object_level_compare_type = object_level_compare_type
        if data_level_compare_info is not None:
            self.data_level_compare_info = data_level_compare_info

    @property
    def job_id(self):
        """Gets the job_id of this CreateCompareTaskReq.

        任务id。

        :return: The job_id of this CreateCompareTaskReq.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this CreateCompareTaskReq.

        任务id。

        :param job_id: The job_id of this CreateCompareTaskReq.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def object_level_compare_type(self):
        """Gets the object_level_compare_type of this CreateCompareTaskReq.

        对象级对比类型，取值为空代表不创建对象级对比。object_level_compare_type和data_level_compare_info都为空时，只查询已创建的对比任务列表。

        :return: The object_level_compare_type of this CreateCompareTaskReq.
        :rtype: str
        """
        return self._object_level_compare_type

    @object_level_compare_type.setter
    def object_level_compare_type(self, object_level_compare_type):
        """Sets the object_level_compare_type of this CreateCompareTaskReq.

        对象级对比类型，取值为空代表不创建对象级对比。object_level_compare_type和data_level_compare_info都为空时，只查询已创建的对比任务列表。

        :param object_level_compare_type: The object_level_compare_type of this CreateCompareTaskReq.
        :type object_level_compare_type: str
        """
        self._object_level_compare_type = object_level_compare_type

    @property
    def data_level_compare_info(self):
        """Gets the data_level_compare_info of this CreateCompareTaskReq.


        :return: The data_level_compare_info of this CreateCompareTaskReq.
        :rtype: :class:`huaweicloudsdkdrs.v3.CreateDataLevelCompareReq`
        """
        return self._data_level_compare_info

    @data_level_compare_info.setter
    def data_level_compare_info(self, data_level_compare_info):
        """Sets the data_level_compare_info of this CreateCompareTaskReq.


        :param data_level_compare_info: The data_level_compare_info of this CreateCompareTaskReq.
        :type data_level_compare_info: :class:`huaweicloudsdkdrs.v3.CreateDataLevelCompareReq`
        """
        self._data_level_compare_info = data_level_compare_info

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
        if not isinstance(other, CreateCompareTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
