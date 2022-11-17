# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportJobsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_list': 'list[str]',
        'export_depend': 'bool'
    }

    attribute_map = {
        'job_list': 'jobList',
        'export_depend': 'exportDepend'
    }

    def __init__(self, job_list=None, export_depend=None):
        """ExportJobsReq

        The model defined in huaweicloud sdk

        :param job_list: 
        :type job_list: list[str]
        :param export_depend: 是否导出作业依赖的脚本和资源
        :type export_depend: bool
        """
        
        

        self._job_list = None
        self._export_depend = None
        self.discriminator = None

        if job_list is not None:
            self.job_list = job_list
        if export_depend is not None:
            self.export_depend = export_depend

    @property
    def job_list(self):
        """Gets the job_list of this ExportJobsReq.

        :return: The job_list of this ExportJobsReq.
        :rtype: list[str]
        """
        return self._job_list

    @job_list.setter
    def job_list(self, job_list):
        """Sets the job_list of this ExportJobsReq.

        :param job_list: The job_list of this ExportJobsReq.
        :type job_list: list[str]
        """
        self._job_list = job_list

    @property
    def export_depend(self):
        """Gets the export_depend of this ExportJobsReq.

        是否导出作业依赖的脚本和资源

        :return: The export_depend of this ExportJobsReq.
        :rtype: bool
        """
        return self._export_depend

    @export_depend.setter
    def export_depend(self, export_depend):
        """Sets the export_depend of this ExportJobsReq.

        是否导出作业依赖的脚本和资源

        :param export_depend: The export_depend of this ExportJobsReq.
        :type export_depend: bool
        """
        self._export_depend = export_depend

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
        if not isinstance(other, ExportJobsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
