# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'max_platform_flavor': 'TaskResourceDto',
        'app_infos': 'list[AppFilterDto]',
        'job_info': 'JobFilterDto'
    }

    attribute_map = {
        'id': 'id',
        'max_platform_flavor': 'max_platform_flavor',
        'app_infos': 'app_infos',
        'job_info': 'job_info'
    }

    def __init__(self, id=None, max_platform_flavor=None, app_infos=None, job_info=None):
        r"""ExecuteJobResponse

        The model defined in huaweicloud sdk

        :param id: 作业id
        :type id: str
        :param max_platform_flavor: 
        :type max_platform_flavor: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        :param app_infos: 筛选后的app集合
        :type app_infos: list[:class:`huaweicloudsdkeihealth.v1.AppFilterDto`]
        :param job_info: 
        :type job_info: :class:`huaweicloudsdkeihealth.v1.JobFilterDto`
        """
        
        super(ExecuteJobResponse, self).__init__()

        self._id = None
        self._max_platform_flavor = None
        self._app_infos = None
        self._job_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if max_platform_flavor is not None:
            self.max_platform_flavor = max_platform_flavor
        if app_infos is not None:
            self.app_infos = app_infos
        if job_info is not None:
            self.job_info = job_info

    @property
    def id(self):
        r"""Gets the id of this ExecuteJobResponse.

        作业id

        :return: The id of this ExecuteJobResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ExecuteJobResponse.

        作业id

        :param id: The id of this ExecuteJobResponse.
        :type id: str
        """
        self._id = id

    @property
    def max_platform_flavor(self):
        r"""Gets the max_platform_flavor of this ExecuteJobResponse.

        :return: The max_platform_flavor of this ExecuteJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        """
        return self._max_platform_flavor

    @max_platform_flavor.setter
    def max_platform_flavor(self, max_platform_flavor):
        r"""Sets the max_platform_flavor of this ExecuteJobResponse.

        :param max_platform_flavor: The max_platform_flavor of this ExecuteJobResponse.
        :type max_platform_flavor: :class:`huaweicloudsdkeihealth.v1.TaskResourceDto`
        """
        self._max_platform_flavor = max_platform_flavor

    @property
    def app_infos(self):
        r"""Gets the app_infos of this ExecuteJobResponse.

        筛选后的app集合

        :return: The app_infos of this ExecuteJobResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.AppFilterDto`]
        """
        return self._app_infos

    @app_infos.setter
    def app_infos(self, app_infos):
        r"""Sets the app_infos of this ExecuteJobResponse.

        筛选后的app集合

        :param app_infos: The app_infos of this ExecuteJobResponse.
        :type app_infos: list[:class:`huaweicloudsdkeihealth.v1.AppFilterDto`]
        """
        self._app_infos = app_infos

    @property
    def job_info(self):
        r"""Gets the job_info of this ExecuteJobResponse.

        :return: The job_info of this ExecuteJobResponse.
        :rtype: :class:`huaweicloudsdkeihealth.v1.JobFilterDto`
        """
        return self._job_info

    @job_info.setter
    def job_info(self, job_info):
        r"""Sets the job_info of this ExecuteJobResponse.

        :param job_info: The job_info of this ExecuteJobResponse.
        :type job_info: :class:`huaweicloudsdkeihealth.v1.JobFilterDto`
        """
        self._job_info = job_info

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
        if not isinstance(other, ExecuteJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
