# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsScanResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'bucket_id': 'str',
        'bucket_name': 'str',
        'file_path': 'str',
        'file_name': 'str',
        'md5': 'str',
        'risk_level': 'int',
        'sensitive_data_type': 'list[str]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'bucket_id': 'bucket_id',
        'bucket_name': 'bucket_name',
        'file_path': 'file_path',
        'file_name': 'file_name',
        'md5': 'md5',
        'risk_level': 'risk_level',
        'sensitive_data_type': 'sensitive_data_type'
    }

    def __init__(self, task_id=None, bucket_id=None, bucket_name=None, file_path=None, file_name=None, md5=None, risk_level=None, sensitive_data_type=None):
        """ObsScanResultInfo

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param bucket_id: OBS桶ID
        :type bucket_id: str
        :param bucket_name: OBS桶名称
        :type bucket_name: str
        :param file_path: 文件路径
        :type file_path: str
        :param file_name: 文件名
        :type file_name: str
        :param md5: 文件md5值
        :type md5: str
        :param risk_level: 风险等级
        :type risk_level: int
        :param sensitive_data_type: 风险数据类型
        :type sensitive_data_type: list[str]
        """
        
        

        self._task_id = None
        self._bucket_id = None
        self._bucket_name = None
        self._file_path = None
        self._file_name = None
        self._md5 = None
        self._risk_level = None
        self._sensitive_data_type = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if bucket_id is not None:
            self.bucket_id = bucket_id
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if file_path is not None:
            self.file_path = file_path
        if file_name is not None:
            self.file_name = file_name
        if md5 is not None:
            self.md5 = md5
        if risk_level is not None:
            self.risk_level = risk_level
        if sensitive_data_type is not None:
            self.sensitive_data_type = sensitive_data_type

    @property
    def task_id(self):
        """Gets the task_id of this ObsScanResultInfo.

        任务ID

        :return: The task_id of this ObsScanResultInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this ObsScanResultInfo.

        任务ID

        :param task_id: The task_id of this ObsScanResultInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def bucket_id(self):
        """Gets the bucket_id of this ObsScanResultInfo.

        OBS桶ID

        :return: The bucket_id of this ObsScanResultInfo.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """Sets the bucket_id of this ObsScanResultInfo.

        OBS桶ID

        :param bucket_id: The bucket_id of this ObsScanResultInfo.
        :type bucket_id: str
        """
        self._bucket_id = bucket_id

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ObsScanResultInfo.

        OBS桶名称

        :return: The bucket_name of this ObsScanResultInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ObsScanResultInfo.

        OBS桶名称

        :param bucket_name: The bucket_name of this ObsScanResultInfo.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def file_path(self):
        """Gets the file_path of this ObsScanResultInfo.

        文件路径

        :return: The file_path of this ObsScanResultInfo.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        """Sets the file_path of this ObsScanResultInfo.

        文件路径

        :param file_path: The file_path of this ObsScanResultInfo.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def file_name(self):
        """Gets the file_name of this ObsScanResultInfo.

        文件名

        :return: The file_name of this ObsScanResultInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ObsScanResultInfo.

        文件名

        :param file_name: The file_name of this ObsScanResultInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def md5(self):
        """Gets the md5 of this ObsScanResultInfo.

        文件md5值

        :return: The md5 of this ObsScanResultInfo.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        """Sets the md5 of this ObsScanResultInfo.

        文件md5值

        :param md5: The md5 of this ObsScanResultInfo.
        :type md5: str
        """
        self._md5 = md5

    @property
    def risk_level(self):
        """Gets the risk_level of this ObsScanResultInfo.

        风险等级

        :return: The risk_level of this ObsScanResultInfo.
        :rtype: int
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """Sets the risk_level of this ObsScanResultInfo.

        风险等级

        :param risk_level: The risk_level of this ObsScanResultInfo.
        :type risk_level: int
        """
        self._risk_level = risk_level

    @property
    def sensitive_data_type(self):
        """Gets the sensitive_data_type of this ObsScanResultInfo.

        风险数据类型

        :return: The sensitive_data_type of this ObsScanResultInfo.
        :rtype: list[str]
        """
        return self._sensitive_data_type

    @sensitive_data_type.setter
    def sensitive_data_type(self, sensitive_data_type):
        """Sets the sensitive_data_type of this ObsScanResultInfo.

        风险数据类型

        :param sensitive_data_type: The sensitive_data_type of this ObsScanResultInfo.
        :type sensitive_data_type: list[str]
        """
        self._sensitive_data_type = sensitive_data_type

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
        if not isinstance(other, ObsScanResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
