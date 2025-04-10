# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateResOnlineInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'description': 'str',
        'category': 'str',
        'job_type': 'str',
        'job_config': 'JobConfig',
        'topic_urn': 'str'
    }

    attribute_map = {
        'job_name': 'job_name',
        'description': 'description',
        'category': 'category',
        'job_type': 'job_type',
        'job_config': 'job_config',
        'topic_urn': 'topicUrn'
    }

    def __init__(self, job_name=None, description=None, category=None, job_type=None, job_config=None, topic_urn=None):
        r"""CreateResOnlineInstanceRequestBody

        The model defined in huaweicloud sdk

        :param job_name: 作业名称，1-64位的字母、数字、下划线、中划线组合。
        :type job_name: str
        :param description: 描述。
        :type description: str
        :param category: 类别: - SERVICE，在线服务
        :type category: str
        :param job_type: 作业类型： - infer，推理服务
        :type job_type: str
        :param job_config: 
        :type job_config: :class:`huaweicloudsdkres.v1.JobConfig`
        :param topic_urn: 通知消息配置。
        :type topic_urn: str
        """
        
        

        self._job_name = None
        self._description = None
        self._category = None
        self._job_type = None
        self._job_config = None
        self._topic_urn = None
        self.discriminator = None

        self.job_name = job_name
        if description is not None:
            self.description = description
        self.category = category
        self.job_type = job_type
        self.job_config = job_config
        if topic_urn is not None:
            self.topic_urn = topic_urn

    @property
    def job_name(self):
        r"""Gets the job_name of this CreateResOnlineInstanceRequestBody.

        作业名称，1-64位的字母、数字、下划线、中划线组合。

        :return: The job_name of this CreateResOnlineInstanceRequestBody.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this CreateResOnlineInstanceRequestBody.

        作业名称，1-64位的字母、数字、下划线、中划线组合。

        :param job_name: The job_name of this CreateResOnlineInstanceRequestBody.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def description(self):
        r"""Gets the description of this CreateResOnlineInstanceRequestBody.

        描述。

        :return: The description of this CreateResOnlineInstanceRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateResOnlineInstanceRequestBody.

        描述。

        :param description: The description of this CreateResOnlineInstanceRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def category(self):
        r"""Gets the category of this CreateResOnlineInstanceRequestBody.

        类别: - SERVICE，在线服务

        :return: The category of this CreateResOnlineInstanceRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateResOnlineInstanceRequestBody.

        类别: - SERVICE，在线服务

        :param category: The category of this CreateResOnlineInstanceRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def job_type(self):
        r"""Gets the job_type of this CreateResOnlineInstanceRequestBody.

        作业类型： - infer，推理服务

        :return: The job_type of this CreateResOnlineInstanceRequestBody.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this CreateResOnlineInstanceRequestBody.

        作业类型： - infer，推理服务

        :param job_type: The job_type of this CreateResOnlineInstanceRequestBody.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_config(self):
        r"""Gets the job_config of this CreateResOnlineInstanceRequestBody.

        :return: The job_config of this CreateResOnlineInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkres.v1.JobConfig`
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        r"""Sets the job_config of this CreateResOnlineInstanceRequestBody.

        :param job_config: The job_config of this CreateResOnlineInstanceRequestBody.
        :type job_config: :class:`huaweicloudsdkres.v1.JobConfig`
        """
        self._job_config = job_config

    @property
    def topic_urn(self):
        r"""Gets the topic_urn of this CreateResOnlineInstanceRequestBody.

        通知消息配置。

        :return: The topic_urn of this CreateResOnlineInstanceRequestBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        r"""Sets the topic_urn of this CreateResOnlineInstanceRequestBody.

        通知消息配置。

        :param topic_urn: The topic_urn of this CreateResOnlineInstanceRequestBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

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
        if not isinstance(other, CreateResOnlineInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
