# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEngineJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_enterprise_project_id': 'str',
        'engine_id': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'x_enterprise_project_id': 'X-Enterprise-Project-ID',
        'engine_id': 'engine_id',
        'job_id': 'job_id'
    }

    def __init__(self, x_enterprise_project_id=None, engine_id=None, job_id=None):
        r"""ShowEngineJobRequest

        The model defined in huaweicloud sdk

        :param x_enterprise_project_id: 如果不带则默认企业项目为\&quot;default\&quot;，ID为\&quot;0\&quot;。
        :type x_enterprise_project_id: str
        :param engine_id: 微服务引擎ID。
        :type engine_id: str
        :param job_id: 任务ID。
        :type job_id: str
        """
        
        

        self._x_enterprise_project_id = None
        self._engine_id = None
        self._job_id = None
        self.discriminator = None

        if x_enterprise_project_id is not None:
            self.x_enterprise_project_id = x_enterprise_project_id
        self.engine_id = engine_id
        self.job_id = job_id

    @property
    def x_enterprise_project_id(self):
        r"""Gets the x_enterprise_project_id of this ShowEngineJobRequest.

        如果不带则默认企业项目为\"default\"，ID为\"0\"。

        :return: The x_enterprise_project_id of this ShowEngineJobRequest.
        :rtype: str
        """
        return self._x_enterprise_project_id

    @x_enterprise_project_id.setter
    def x_enterprise_project_id(self, x_enterprise_project_id):
        r"""Sets the x_enterprise_project_id of this ShowEngineJobRequest.

        如果不带则默认企业项目为\"default\"，ID为\"0\"。

        :param x_enterprise_project_id: The x_enterprise_project_id of this ShowEngineJobRequest.
        :type x_enterprise_project_id: str
        """
        self._x_enterprise_project_id = x_enterprise_project_id

    @property
    def engine_id(self):
        r"""Gets the engine_id of this ShowEngineJobRequest.

        微服务引擎ID。

        :return: The engine_id of this ShowEngineJobRequest.
        :rtype: str
        """
        return self._engine_id

    @engine_id.setter
    def engine_id(self, engine_id):
        r"""Sets the engine_id of this ShowEngineJobRequest.

        微服务引擎ID。

        :param engine_id: The engine_id of this ShowEngineJobRequest.
        :type engine_id: str
        """
        self._engine_id = engine_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowEngineJobRequest.

        任务ID。

        :return: The job_id of this ShowEngineJobRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowEngineJobRequest.

        任务ID。

        :param job_id: The job_id of this ShowEngineJobRequest.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, ShowEngineJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
