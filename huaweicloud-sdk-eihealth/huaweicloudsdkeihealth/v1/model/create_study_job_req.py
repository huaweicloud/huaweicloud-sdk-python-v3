# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateStudyJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflow_job_id': 'str',
        'template_id': 'str',
        'database_name': 'str',
        'relative_path': 'str',
        'output_file_type': 'OutputFileType'
    }

    attribute_map = {
        'workflow_job_id': 'workflow_job_id',
        'template_id': 'template_id',
        'database_name': 'database_name',
        'relative_path': 'relative_path',
        'output_file_type': 'output_file_type'
    }

    def __init__(self, workflow_job_id=None, template_id=None, database_name=None, relative_path=None, output_file_type=None):
        """CreateStudyJobReq

        The model defined in huaweicloud sdk

        :param workflow_job_id: workflow作业id
        :type workflow_job_id: str
        :param template_id: 数据库模板id
        :type template_id: str
        :param database_name: 数据库名称
        :type database_name: str
        :param relative_path: 生成数据库实例的文件相对路径
        :type relative_path: str
        :param output_file_type: 
        :type output_file_type: :class:`huaweicloudsdkeihealth.v1.OutputFileType`
        """
        
        

        self._workflow_job_id = None
        self._template_id = None
        self._database_name = None
        self._relative_path = None
        self._output_file_type = None
        self.discriminator = None

        self.workflow_job_id = workflow_job_id
        if template_id is not None:
            self.template_id = template_id
        self.database_name = database_name
        self.relative_path = relative_path
        self.output_file_type = output_file_type

    @property
    def workflow_job_id(self):
        """Gets the workflow_job_id of this CreateStudyJobReq.

        workflow作业id

        :return: The workflow_job_id of this CreateStudyJobReq.
        :rtype: str
        """
        return self._workflow_job_id

    @workflow_job_id.setter
    def workflow_job_id(self, workflow_job_id):
        """Sets the workflow_job_id of this CreateStudyJobReq.

        workflow作业id

        :param workflow_job_id: The workflow_job_id of this CreateStudyJobReq.
        :type workflow_job_id: str
        """
        self._workflow_job_id = workflow_job_id

    @property
    def template_id(self):
        """Gets the template_id of this CreateStudyJobReq.

        数据库模板id

        :return: The template_id of this CreateStudyJobReq.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateStudyJobReq.

        数据库模板id

        :param template_id: The template_id of this CreateStudyJobReq.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def database_name(self):
        """Gets the database_name of this CreateStudyJobReq.

        数据库名称

        :return: The database_name of this CreateStudyJobReq.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this CreateStudyJobReq.

        数据库名称

        :param database_name: The database_name of this CreateStudyJobReq.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def relative_path(self):
        """Gets the relative_path of this CreateStudyJobReq.

        生成数据库实例的文件相对路径

        :return: The relative_path of this CreateStudyJobReq.
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this CreateStudyJobReq.

        生成数据库实例的文件相对路径

        :param relative_path: The relative_path of this CreateStudyJobReq.
        :type relative_path: str
        """
        self._relative_path = relative_path

    @property
    def output_file_type(self):
        """Gets the output_file_type of this CreateStudyJobReq.

        :return: The output_file_type of this CreateStudyJobReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.OutputFileType`
        """
        return self._output_file_type

    @output_file_type.setter
    def output_file_type(self, output_file_type):
        """Sets the output_file_type of this CreateStudyJobReq.

        :param output_file_type: The output_file_type of this CreateStudyJobReq.
        :type output_file_type: :class:`huaweicloudsdkeihealth.v1.OutputFileType`
        """
        self._output_file_type = output_file_type

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
        if not isinstance(other, CreateStudyJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
