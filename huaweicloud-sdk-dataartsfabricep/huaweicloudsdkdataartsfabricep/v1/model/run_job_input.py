# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunJobInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job': 'JobRef',
        'name': 'str',
        'endpoint_id': 'str'
    }

    attribute_map = {
        'job': 'job',
        'name': 'name',
        'endpoint_id': 'endpoint_id'
    }

    def __init__(self, job=None, name=None, endpoint_id=None):
        r"""RunJobInput

        The model defined in huaweicloud sdk

        :param job: 
        :type job: :class:`huaweicloudsdkdataartsfabricep.v1.JobRef`
        :param name: 作业运行的名称，只能包含中文、字母、数字、下划线、中划线、点、空格
        :type name: str
        :param endpoint_id: endpoint空间id
        :type endpoint_id: str
        """
        
        

        self._job = None
        self._name = None
        self._endpoint_id = None
        self.discriminator = None

        self.job = job
        self.name = name
        self.endpoint_id = endpoint_id

    @property
    def job(self):
        r"""Gets the job of this RunJobInput.

        :return: The job of this RunJobInput.
        :rtype: :class:`huaweicloudsdkdataartsfabricep.v1.JobRef`
        """
        return self._job

    @job.setter
    def job(self, job):
        r"""Sets the job of this RunJobInput.

        :param job: The job of this RunJobInput.
        :type job: :class:`huaweicloudsdkdataartsfabricep.v1.JobRef`
        """
        self._job = job

    @property
    def name(self):
        r"""Gets the name of this RunJobInput.

        作业运行的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :return: The name of this RunJobInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RunJobInput.

        作业运行的名称，只能包含中文、字母、数字、下划线、中划线、点、空格

        :param name: The name of this RunJobInput.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this RunJobInput.

        endpoint空间id

        :return: The endpoint_id of this RunJobInput.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this RunJobInput.

        endpoint空间id

        :param endpoint_id: The endpoint_id of this RunJobInput.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RunJobInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
