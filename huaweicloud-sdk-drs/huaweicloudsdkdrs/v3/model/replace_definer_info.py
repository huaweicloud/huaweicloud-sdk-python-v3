# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReplaceDefinerInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'replace_definer': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'replace_definer': 'replace_definer'
    }

    def __init__(self, job_id=None, replace_definer=None):
        """ReplaceDefinerInfo

        The model defined in huaweicloud sdk

        :param job_id: 任务id
        :type job_id: str
        :param replace_definer: 是否使用目标库的用户替换掉definer
        :type replace_definer: bool
        """
        
        

        self._job_id = None
        self._replace_definer = None
        self.discriminator = None

        self.job_id = job_id
        self.replace_definer = replace_definer

    @property
    def job_id(self):
        """Gets the job_id of this ReplaceDefinerInfo.

        任务id

        :return: The job_id of this ReplaceDefinerInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ReplaceDefinerInfo.

        任务id

        :param job_id: The job_id of this ReplaceDefinerInfo.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def replace_definer(self):
        """Gets the replace_definer of this ReplaceDefinerInfo.

        是否使用目标库的用户替换掉definer

        :return: The replace_definer of this ReplaceDefinerInfo.
        :rtype: bool
        """
        return self._replace_definer

    @replace_definer.setter
    def replace_definer(self, replace_definer):
        """Sets the replace_definer of this ReplaceDefinerInfo.

        是否使用目标库的用户替换掉definer

        :param replace_definer: The replace_definer of this ReplaceDefinerInfo.
        :type replace_definer: bool
        """
        self._replace_definer = replace_definer

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
        if not isinstance(other, ReplaceDefinerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
