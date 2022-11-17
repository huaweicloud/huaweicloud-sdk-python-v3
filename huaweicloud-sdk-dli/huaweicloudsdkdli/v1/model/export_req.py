# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'obs_dir': 'str',
        'is_selected': 'bool',
        'job_selected': 'list[int]'
    }

    attribute_map = {
        'obs_dir': 'obs_dir',
        'is_selected': 'is_selected',
        'job_selected': 'job_selected'
    }

    def __init__(self, obs_dir=None, is_selected=None, job_selected=None):
        """ExportReq

        The model defined in huaweicloud sdk

        :param obs_dir: 导出作业文件的OBS保存路径。
        :type obs_dir: str
        :param is_selected: 是否导出指定的作业。
        :type is_selected: bool
        :param job_selected: 当is_selected&#x3D;true时，该参数是待导出作业的作业ID集合。当is_selected&#x3D;true时，此参数必填。
        :type job_selected: list[int]
        """
        
        

        self._obs_dir = None
        self._is_selected = None
        self._job_selected = None
        self.discriminator = None

        self.obs_dir = obs_dir
        self.is_selected = is_selected
        if job_selected is not None:
            self.job_selected = job_selected

    @property
    def obs_dir(self):
        """Gets the obs_dir of this ExportReq.

        导出作业文件的OBS保存路径。

        :return: The obs_dir of this ExportReq.
        :rtype: str
        """
        return self._obs_dir

    @obs_dir.setter
    def obs_dir(self, obs_dir):
        """Sets the obs_dir of this ExportReq.

        导出作业文件的OBS保存路径。

        :param obs_dir: The obs_dir of this ExportReq.
        :type obs_dir: str
        """
        self._obs_dir = obs_dir

    @property
    def is_selected(self):
        """Gets the is_selected of this ExportReq.

        是否导出指定的作业。

        :return: The is_selected of this ExportReq.
        :rtype: bool
        """
        return self._is_selected

    @is_selected.setter
    def is_selected(self, is_selected):
        """Sets the is_selected of this ExportReq.

        是否导出指定的作业。

        :param is_selected: The is_selected of this ExportReq.
        :type is_selected: bool
        """
        self._is_selected = is_selected

    @property
    def job_selected(self):
        """Gets the job_selected of this ExportReq.

        当is_selected=true时，该参数是待导出作业的作业ID集合。当is_selected=true时，此参数必填。

        :return: The job_selected of this ExportReq.
        :rtype: list[int]
        """
        return self._job_selected

    @job_selected.setter
    def job_selected(self, job_selected):
        """Sets the job_selected of this ExportReq.

        当is_selected=true时，该参数是待导出作业的作业ID集合。当is_selected=true时，此参数必填。

        :param job_selected: The job_selected of this ExportReq.
        :type job_selected: list[int]
        """
        self._job_selected = job_selected

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
        if not isinstance(other, ExportReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
