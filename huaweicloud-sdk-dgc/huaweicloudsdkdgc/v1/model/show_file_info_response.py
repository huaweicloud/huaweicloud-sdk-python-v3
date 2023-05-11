# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFileInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'jobs': 'list[Job]',
        'scripts': 'list[Script]'
    }

    attribute_map = {
        'jobs': 'jobs',
        'scripts': 'scripts'
    }

    def __init__(self, jobs=None, scripts=None):
        """ShowFileInfoResponse

        The model defined in huaweicloud sdk

        :param jobs: 
        :type jobs: list[:class:`huaweicloudsdkdgc.v1.Job`]
        :param scripts: 
        :type scripts: list[:class:`huaweicloudsdkdgc.v1.Script`]
        """
        
        super(ShowFileInfoResponse, self).__init__()

        self._jobs = None
        self._scripts = None
        self.discriminator = None

        if jobs is not None:
            self.jobs = jobs
        if scripts is not None:
            self.scripts = scripts

    @property
    def jobs(self):
        """Gets the jobs of this ShowFileInfoResponse.

        :return: The jobs of this ShowFileInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.Job`]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs):
        """Sets the jobs of this ShowFileInfoResponse.

        :param jobs: The jobs of this ShowFileInfoResponse.
        :type jobs: list[:class:`huaweicloudsdkdgc.v1.Job`]
        """
        self._jobs = jobs

    @property
    def scripts(self):
        """Gets the scripts of this ShowFileInfoResponse.

        :return: The scripts of this ShowFileInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.Script`]
        """
        return self._scripts

    @scripts.setter
    def scripts(self, scripts):
        """Sets the scripts of this ShowFileInfoResponse.

        :param scripts: The scripts of this ShowFileInfoResponse.
        :type scripts: list[:class:`huaweicloudsdkdgc.v1.Script`]
        """
        self._scripts = scripts

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
        if not isinstance(other, ShowFileInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
