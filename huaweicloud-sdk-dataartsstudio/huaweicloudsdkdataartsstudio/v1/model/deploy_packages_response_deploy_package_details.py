# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeployPackagesResponseDeployPackageDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asy_subtask_num': 'int',
        'asy_task_id': 'str',
        'package_id': 'int'
    }

    attribute_map = {
        'asy_subtask_num': 'asy_subtask_num',
        'asy_task_id': 'asy_task_id',
        'package_id': 'package_id'
    }

    def __init__(self, asy_subtask_num=None, asy_task_id=None, package_id=None):
        """DeployPackagesResponseDeployPackageDetails

        The model defined in huaweicloud sdk

        :param asy_subtask_num: 总的异步执行的子任务个数
        :type asy_subtask_num: int
        :param asy_task_id: 异步作业id，返回给前台轮询结果
        :type asy_task_id: str
        :param package_id: 发布包ID
        :type package_id: int
        """
        
        

        self._asy_subtask_num = None
        self._asy_task_id = None
        self._package_id = None
        self.discriminator = None

        if asy_subtask_num is not None:
            self.asy_subtask_num = asy_subtask_num
        if asy_task_id is not None:
            self.asy_task_id = asy_task_id
        if package_id is not None:
            self.package_id = package_id

    @property
    def asy_subtask_num(self):
        """Gets the asy_subtask_num of this DeployPackagesResponseDeployPackageDetails.

        总的异步执行的子任务个数

        :return: The asy_subtask_num of this DeployPackagesResponseDeployPackageDetails.
        :rtype: int
        """
        return self._asy_subtask_num

    @asy_subtask_num.setter
    def asy_subtask_num(self, asy_subtask_num):
        """Sets the asy_subtask_num of this DeployPackagesResponseDeployPackageDetails.

        总的异步执行的子任务个数

        :param asy_subtask_num: The asy_subtask_num of this DeployPackagesResponseDeployPackageDetails.
        :type asy_subtask_num: int
        """
        self._asy_subtask_num = asy_subtask_num

    @property
    def asy_task_id(self):
        """Gets the asy_task_id of this DeployPackagesResponseDeployPackageDetails.

        异步作业id，返回给前台轮询结果

        :return: The asy_task_id of this DeployPackagesResponseDeployPackageDetails.
        :rtype: str
        """
        return self._asy_task_id

    @asy_task_id.setter
    def asy_task_id(self, asy_task_id):
        """Sets the asy_task_id of this DeployPackagesResponseDeployPackageDetails.

        异步作业id，返回给前台轮询结果

        :param asy_task_id: The asy_task_id of this DeployPackagesResponseDeployPackageDetails.
        :type asy_task_id: str
        """
        self._asy_task_id = asy_task_id

    @property
    def package_id(self):
        """Gets the package_id of this DeployPackagesResponseDeployPackageDetails.

        发布包ID

        :return: The package_id of this DeployPackagesResponseDeployPackageDetails.
        :rtype: int
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this DeployPackagesResponseDeployPackageDetails.

        发布包ID

        :param package_id: The package_id of this DeployPackagesResponseDeployPackageDetails.
        :type package_id: int
        """
        self._package_id = package_id

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
        if not isinstance(other, DeployPackagesResponseDeployPackageDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
