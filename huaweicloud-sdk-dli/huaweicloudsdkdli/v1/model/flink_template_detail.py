# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkTemplateDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'int',
        'name': 'str',
        'desc': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'sql_body': 'str',
        'job_type': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'name': 'name',
        'desc': 'desc',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'sql_body': 'sql_body',
        'job_type': 'job_type'
    }

    def __init__(self, template_id=None, name=None, desc=None, create_time=None, update_time=None, sql_body=None, job_type=None):
        """FlinkTemplateDetail

        The model defined in huaweicloud sdk

        :param template_id: 模板ID。
        :type template_id: int
        :param name: 模板名称。
        :type name: str
        :param desc: 模板描述。
        :type desc: str
        :param create_time: 模板创建时间。
        :type create_time: int
        :param update_time: 模板更新时间。
        :type update_time: int
        :param sql_body: Stream SQL语句, 至少包含source, query, sink三个部分。
        :type sql_body: str
        :param job_type: 作业模板的类型。
        :type job_type: str
        """
        
        

        self._template_id = None
        self._name = None
        self._desc = None
        self._create_time = None
        self._update_time = None
        self._sql_body = None
        self._job_type = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if sql_body is not None:
            self.sql_body = sql_body
        if job_type is not None:
            self.job_type = job_type

    @property
    def template_id(self):
        """Gets the template_id of this FlinkTemplateDetail.

        模板ID。

        :return: The template_id of this FlinkTemplateDetail.
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this FlinkTemplateDetail.

        模板ID。

        :param template_id: The template_id of this FlinkTemplateDetail.
        :type template_id: int
        """
        self._template_id = template_id

    @property
    def name(self):
        """Gets the name of this FlinkTemplateDetail.

        模板名称。

        :return: The name of this FlinkTemplateDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlinkTemplateDetail.

        模板名称。

        :param name: The name of this FlinkTemplateDetail.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        """Gets the desc of this FlinkTemplateDetail.

        模板描述。

        :return: The desc of this FlinkTemplateDetail.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        """Sets the desc of this FlinkTemplateDetail.

        模板描述。

        :param desc: The desc of this FlinkTemplateDetail.
        :type desc: str
        """
        self._desc = desc

    @property
    def create_time(self):
        """Gets the create_time of this FlinkTemplateDetail.

        模板创建时间。

        :return: The create_time of this FlinkTemplateDetail.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this FlinkTemplateDetail.

        模板创建时间。

        :param create_time: The create_time of this FlinkTemplateDetail.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this FlinkTemplateDetail.

        模板更新时间。

        :return: The update_time of this FlinkTemplateDetail.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this FlinkTemplateDetail.

        模板更新时间。

        :param update_time: The update_time of this FlinkTemplateDetail.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def sql_body(self):
        """Gets the sql_body of this FlinkTemplateDetail.

        Stream SQL语句, 至少包含source, query, sink三个部分。

        :return: The sql_body of this FlinkTemplateDetail.
        :rtype: str
        """
        return self._sql_body

    @sql_body.setter
    def sql_body(self, sql_body):
        """Sets the sql_body of this FlinkTemplateDetail.

        Stream SQL语句, 至少包含source, query, sink三个部分。

        :param sql_body: The sql_body of this FlinkTemplateDetail.
        :type sql_body: str
        """
        self._sql_body = sql_body

    @property
    def job_type(self):
        """Gets the job_type of this FlinkTemplateDetail.

        作业模板的类型。

        :return: The job_type of this FlinkTemplateDetail.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this FlinkTemplateDetail.

        作业模板的类型。

        :param job_type: The job_type of this FlinkTemplateDetail.
        :type job_type: str
        """
        self._job_type = job_type

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
        if not isinstance(other, FlinkTemplateDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
