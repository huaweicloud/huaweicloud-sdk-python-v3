# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEncryptFileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('once_token')

    openapi_types = {
        'tenant_id': 'str',
        'job_id': 'str',
        'once_token': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'job_id': 'job_id',
        'once_token': 'once_token'
    }

    def __init__(self, tenant_id=None, job_id=None, once_token=None):
        r"""ShowEncryptFileRequest

        The model defined in huaweicloud sdk

        :param tenant_id: 租户id
        :type tenant_id: str
        :param job_id: 任务id
        :type job_id: str
        :param once_token: 一次性token
        :type once_token: str
        """
        
        

        self._tenant_id = None
        self._job_id = None
        self._once_token = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.job_id = job_id
        self.once_token = once_token

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this ShowEncryptFileRequest.

        租户id

        :return: The tenant_id of this ShowEncryptFileRequest.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this ShowEncryptFileRequest.

        租户id

        :param tenant_id: The tenant_id of this ShowEncryptFileRequest.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowEncryptFileRequest.

        任务id

        :return: The job_id of this ShowEncryptFileRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowEncryptFileRequest.

        任务id

        :param job_id: The job_id of this ShowEncryptFileRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def once_token(self):
        r"""Gets the once_token of this ShowEncryptFileRequest.

        一次性token

        :return: The once_token of this ShowEncryptFileRequest.
        :rtype: str
        """
        return self._once_token

    @once_token.setter
    def once_token(self, once_token):
        r"""Sets the once_token of this ShowEncryptFileRequest.

        一次性token

        :param once_token: The once_token of this ShowEncryptFileRequest.
        :type once_token: str
        """
        self._once_token = once_token

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
        if not isinstance(other, ShowEncryptFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
