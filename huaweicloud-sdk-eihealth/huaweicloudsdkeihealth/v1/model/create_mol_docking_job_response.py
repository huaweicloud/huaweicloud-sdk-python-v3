# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMolDockingJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vina_score': 'float',
        'pose': 'str'
    }

    attribute_map = {
        'vina_score': 'vina_score',
        'pose': 'pose'
    }

    def __init__(self, vina_score=None, pose=None):
        r"""CreateMolDockingJobResponse

        The model defined in huaweicloud sdk

        :param vina_score: 对接打分结果。
        :type vina_score: float
        :param pose: 对接构象。
        :type pose: str
        """
        
        super(CreateMolDockingJobResponse, self).__init__()

        self._vina_score = None
        self._pose = None
        self.discriminator = None

        if vina_score is not None:
            self.vina_score = vina_score
        if pose is not None:
            self.pose = pose

    @property
    def vina_score(self):
        r"""Gets the vina_score of this CreateMolDockingJobResponse.

        对接打分结果。

        :return: The vina_score of this CreateMolDockingJobResponse.
        :rtype: float
        """
        return self._vina_score

    @vina_score.setter
    def vina_score(self, vina_score):
        r"""Sets the vina_score of this CreateMolDockingJobResponse.

        对接打分结果。

        :param vina_score: The vina_score of this CreateMolDockingJobResponse.
        :type vina_score: float
        """
        self._vina_score = vina_score

    @property
    def pose(self):
        r"""Gets the pose of this CreateMolDockingJobResponse.

        对接构象。

        :return: The pose of this CreateMolDockingJobResponse.
        :rtype: str
        """
        return self._pose

    @pose.setter
    def pose(self, pose):
        r"""Sets the pose of this CreateMolDockingJobResponse.

        对接构象。

        :param pose: The pose of this CreateMolDockingJobResponse.
        :type pose: str
        """
        self._pose = pose

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
        if not isinstance(other, CreateMolDockingJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
