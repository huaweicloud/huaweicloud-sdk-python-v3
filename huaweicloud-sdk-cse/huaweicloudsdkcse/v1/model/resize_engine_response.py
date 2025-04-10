# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResizeEngineResponse(SdkResponse):

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
        'name': 'str',
        'job_id': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'job_id': 'job_id'
    }

    def __init__(self, id=None, name=None, job_id=None):
        r"""ResizeEngineResponse

        The model defined in huaweicloud sdk

        :param id: 引擎id
        :type id: str
        :param name: 引擎名字
        :type name: str
        :param job_id: jobID
        :type job_id: int
        """
        
        super(ResizeEngineResponse, self).__init__()

        self._id = None
        self._name = None
        self._job_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if job_id is not None:
            self.job_id = job_id

    @property
    def id(self):
        r"""Gets the id of this ResizeEngineResponse.

        引擎id

        :return: The id of this ResizeEngineResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ResizeEngineResponse.

        引擎id

        :param id: The id of this ResizeEngineResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ResizeEngineResponse.

        引擎名字

        :return: The name of this ResizeEngineResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ResizeEngineResponse.

        引擎名字

        :param name: The name of this ResizeEngineResponse.
        :type name: str
        """
        self._name = name

    @property
    def job_id(self):
        r"""Gets the job_id of this ResizeEngineResponse.

        jobID

        :return: The job_id of this ResizeEngineResponse.
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ResizeEngineResponse.

        jobID

        :param job_id: The job_id of this ResizeEngineResponse.
        :type job_id: int
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
        if not isinstance(other, ResizeEngineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
