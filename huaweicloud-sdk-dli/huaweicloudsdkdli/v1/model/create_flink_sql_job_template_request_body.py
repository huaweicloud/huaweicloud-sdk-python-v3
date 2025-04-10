# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFlinkSqlJobTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'desc': 'str',
        'sql_body': 'str',
        'tags': 'list[Tag]',
        'job_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'desc': 'desc',
        'sql_body': 'sql_body',
        'tags': 'tags',
        'job_type': 'job_type'
    }

    def __init__(self, name=None, desc=None, sql_body=None, tags=None, job_type=None):
        r"""CreateFlinkSqlJobTemplateRequestBody

        The model defined in huaweicloud sdk

        :param name: 模块名称，长度限制：0-57个字符 。
        :type name: str
        :param desc: 模板描述，长度限制：0-2048个字符。
        :type desc: str
        :param sql_body: Stream SQL语句，至少包含source，query，sink三个部分, 长度限制：0-2048个字符。
        :type sql_body: str
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        :param job_type: 作业模板的类型，默认为flink_sql_job，仅支持flink_sql_job和flink_opensource_sql_job
        :type job_type: str
        """
        
        

        self._name = None
        self._desc = None
        self._sql_body = None
        self._tags = None
        self._job_type = None
        self.discriminator = None

        self.name = name
        if desc is not None:
            self.desc = desc
        if sql_body is not None:
            self.sql_body = sql_body
        if tags is not None:
            self.tags = tags
        if job_type is not None:
            self.job_type = job_type

    @property
    def name(self):
        r"""Gets the name of this CreateFlinkSqlJobTemplateRequestBody.

        模块名称，长度限制：0-57个字符 。

        :return: The name of this CreateFlinkSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateFlinkSqlJobTemplateRequestBody.

        模块名称，长度限制：0-57个字符 。

        :param name: The name of this CreateFlinkSqlJobTemplateRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        r"""Gets the desc of this CreateFlinkSqlJobTemplateRequestBody.

        模板描述，长度限制：0-2048个字符。

        :return: The desc of this CreateFlinkSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this CreateFlinkSqlJobTemplateRequestBody.

        模板描述，长度限制：0-2048个字符。

        :param desc: The desc of this CreateFlinkSqlJobTemplateRequestBody.
        :type desc: str
        """
        self._desc = desc

    @property
    def sql_body(self):
        r"""Gets the sql_body of this CreateFlinkSqlJobTemplateRequestBody.

        Stream SQL语句，至少包含source，query，sink三个部分, 长度限制：0-2048个字符。

        :return: The sql_body of this CreateFlinkSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._sql_body

    @sql_body.setter
    def sql_body(self, sql_body):
        r"""Sets the sql_body of this CreateFlinkSqlJobTemplateRequestBody.

        Stream SQL语句，至少包含source，query，sink三个部分, 长度限制：0-2048个字符。

        :param sql_body: The sql_body of this CreateFlinkSqlJobTemplateRequestBody.
        :type sql_body: str
        """
        self._sql_body = sql_body

    @property
    def tags(self):
        r"""Gets the tags of this CreateFlinkSqlJobTemplateRequestBody.

        标签

        :return: The tags of this CreateFlinkSqlJobTemplateRequestBody.
        :rtype: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateFlinkSqlJobTemplateRequestBody.

        标签

        :param tags: The tags of this CreateFlinkSqlJobTemplateRequestBody.
        :type tags: list[:class:`huaweicloudsdkdli.v1.Tag`]
        """
        self._tags = tags

    @property
    def job_type(self):
        r"""Gets the job_type of this CreateFlinkSqlJobTemplateRequestBody.

        作业模板的类型，默认为flink_sql_job，仅支持flink_sql_job和flink_opensource_sql_job

        :return: The job_type of this CreateFlinkSqlJobTemplateRequestBody.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this CreateFlinkSqlJobTemplateRequestBody.

        作业模板的类型，默认为flink_sql_job，仅支持flink_sql_job和flink_opensource_sql_job

        :param job_type: The job_type of this CreateFlinkSqlJobTemplateRequestBody.
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
        if not isinstance(other, CreateFlinkSqlJobTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
