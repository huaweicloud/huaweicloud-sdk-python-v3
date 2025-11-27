# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'federation_uid': 'str',
        'resource_id': 'str',
        'resource_name': 'str',
        'extendparam': 'str',
        'sub_jobs': 'list[Job]'
    }

    attribute_map = {
        'type': 'type',
        'federation_uid': 'federationUID',
        'resource_id': 'resourceID',
        'resource_name': 'resourceName',
        'extendparam': 'extendparam',
        'sub_jobs': 'subJobs'
    }

    def __init__(self, type=None, federation_uid=None, resource_id=None, resource_name=None, extendparam=None, sub_jobs=None):
        r"""JobSpec

        The model defined in huaweicloud sdk

        :param type: Job类型
        :type type: str
        :param federation_uid: 联邦uid
        :type federation_uid: str
        :param resource_id: 资源id
        :type resource_id: str
        :param resource_name: 资源名字
        :type resource_name: str
        :param extendparam: 扩展参数
        :type extendparam: str
        :param sub_jobs: 子Job
        :type sub_jobs: list[:class:`huaweicloudsdkucs.v1.Job`]
        """
        
        

        self._type = None
        self._federation_uid = None
        self._resource_id = None
        self._resource_name = None
        self._extendparam = None
        self._sub_jobs = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if federation_uid is not None:
            self.federation_uid = federation_uid
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_name is not None:
            self.resource_name = resource_name
        if extendparam is not None:
            self.extendparam = extendparam
        if sub_jobs is not None:
            self.sub_jobs = sub_jobs

    @property
    def type(self):
        r"""Gets the type of this JobSpec.

        Job类型

        :return: The type of this JobSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this JobSpec.

        Job类型

        :param type: The type of this JobSpec.
        :type type: str
        """
        self._type = type

    @property
    def federation_uid(self):
        r"""Gets the federation_uid of this JobSpec.

        联邦uid

        :return: The federation_uid of this JobSpec.
        :rtype: str
        """
        return self._federation_uid

    @federation_uid.setter
    def federation_uid(self, federation_uid):
        r"""Sets the federation_uid of this JobSpec.

        联邦uid

        :param federation_uid: The federation_uid of this JobSpec.
        :type federation_uid: str
        """
        self._federation_uid = federation_uid

    @property
    def resource_id(self):
        r"""Gets the resource_id of this JobSpec.

        资源id

        :return: The resource_id of this JobSpec.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this JobSpec.

        资源id

        :param resource_id: The resource_id of this JobSpec.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_name(self):
        r"""Gets the resource_name of this JobSpec.

        资源名字

        :return: The resource_name of this JobSpec.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this JobSpec.

        资源名字

        :param resource_name: The resource_name of this JobSpec.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def extendparam(self):
        r"""Gets the extendparam of this JobSpec.

        扩展参数

        :return: The extendparam of this JobSpec.
        :rtype: str
        """
        return self._extendparam

    @extendparam.setter
    def extendparam(self, extendparam):
        r"""Sets the extendparam of this JobSpec.

        扩展参数

        :param extendparam: The extendparam of this JobSpec.
        :type extendparam: str
        """
        self._extendparam = extendparam

    @property
    def sub_jobs(self):
        r"""Gets the sub_jobs of this JobSpec.

        子Job

        :return: The sub_jobs of this JobSpec.
        :rtype: list[:class:`huaweicloudsdkucs.v1.Job`]
        """
        return self._sub_jobs

    @sub_jobs.setter
    def sub_jobs(self, sub_jobs):
        r"""Sets the sub_jobs of this JobSpec.

        子Job

        :param sub_jobs: The sub_jobs of this JobSpec.
        :type sub_jobs: list[:class:`huaweicloudsdkucs.v1.Job`]
        """
        self._sub_jobs = sub_jobs

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
        if not isinstance(other, JobSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
