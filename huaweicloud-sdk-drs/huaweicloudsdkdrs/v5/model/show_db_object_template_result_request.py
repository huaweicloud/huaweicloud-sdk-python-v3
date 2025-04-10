# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDbObjectTemplateResultRequest:

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
        'file_export_object_level': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'x_language': 'X-Language',
        'type': 'type',
        'file_export_object_level': 'file_export_object_level'
    }

    def __init__(self, job_id=None, x_language=None, type=None, file_export_object_level=None):
        r"""ShowDbObjectTemplateResultRequest

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param type: 导入的结果类型。取值： - detail：获取最新导入的文件与校验结果，上传后的文件若存在错误，会同时将错误原因标记在文件内。 - synchronized：获取已同步的（已下发的）对象文件结果。 - change: 获取新增和删除的对象结果（当再编辑时使用）
        :type type: str
        :param file_export_object_level: 默认为空。当进行列加工导入时，查询列加工导入进度，取值column。
        :type file_export_object_level: str
        """
        
        

        self._job_id = None
        self._x_language = None
        self._type = None
        self._file_export_object_level = None
        self.discriminator = None

        self.job_id = job_id
        if x_language is not None:
            self.x_language = x_language
        self.type = type
        if file_export_object_level is not None:
            self.file_export_object_level = file_export_object_level

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowDbObjectTemplateResultRequest.

        任务ID。

        :return: The job_id of this ShowDbObjectTemplateResultRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowDbObjectTemplateResultRequest.

        任务ID。

        :param job_id: The job_id of this ShowDbObjectTemplateResultRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowDbObjectTemplateResultRequest.

        请求语言类型。

        :return: The x_language of this ShowDbObjectTemplateResultRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowDbObjectTemplateResultRequest.

        请求语言类型。

        :param x_language: The x_language of this ShowDbObjectTemplateResultRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def type(self):
        r"""Gets the type of this ShowDbObjectTemplateResultRequest.

        导入的结果类型。取值： - detail：获取最新导入的文件与校验结果，上传后的文件若存在错误，会同时将错误原因标记在文件内。 - synchronized：获取已同步的（已下发的）对象文件结果。 - change: 获取新增和删除的对象结果（当再编辑时使用）

        :return: The type of this ShowDbObjectTemplateResultRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowDbObjectTemplateResultRequest.

        导入的结果类型。取值： - detail：获取最新导入的文件与校验结果，上传后的文件若存在错误，会同时将错误原因标记在文件内。 - synchronized：获取已同步的（已下发的）对象文件结果。 - change: 获取新增和删除的对象结果（当再编辑时使用）

        :param type: The type of this ShowDbObjectTemplateResultRequest.
        :type type: str
        """
        self._type = type

    @property
    def file_export_object_level(self):
        r"""Gets the file_export_object_level of this ShowDbObjectTemplateResultRequest.

        默认为空。当进行列加工导入时，查询列加工导入进度，取值column。

        :return: The file_export_object_level of this ShowDbObjectTemplateResultRequest.
        :rtype: str
        """
        return self._file_export_object_level

    @file_export_object_level.setter
    def file_export_object_level(self, file_export_object_level):
        r"""Sets the file_export_object_level of this ShowDbObjectTemplateResultRequest.

        默认为空。当进行列加工导入时，查询列加工导入进度，取值column。

        :param file_export_object_level: The file_export_object_level of this ShowDbObjectTemplateResultRequest.
        :type file_export_object_level: str
        """
        self._file_export_object_level = file_export_object_level

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
        if not isinstance(other, ShowDbObjectTemplateResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
