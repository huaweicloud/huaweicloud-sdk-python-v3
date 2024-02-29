# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFactoryPackageDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'release_package': 'ShowPackageDetailRespReleasePackage',
        'task_details': 'list[ShowPackageDetailRespTaskDetails]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'release_package': 'release_package',
        'task_details': 'task_details',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, release_package=None, task_details=None, x_request_id=None):
        """ShowFactoryPackageDetailResponse

        The model defined in huaweicloud sdk

        :param release_package: 
        :type release_package: :class:`huaweicloudsdkdataartsstudio.v1.ShowPackageDetailRespReleasePackage`
        :param task_details: 发布任务详情
        :type task_details: list[:class:`huaweicloudsdkdataartsstudio.v1.ShowPackageDetailRespTaskDetails`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowFactoryPackageDetailResponse, self).__init__()

        self._release_package = None
        self._task_details = None
        self._x_request_id = None
        self.discriminator = None

        if release_package is not None:
            self.release_package = release_package
        if task_details is not None:
            self.task_details = task_details
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def release_package(self):
        """Gets the release_package of this ShowFactoryPackageDetailResponse.

        :return: The release_package of this ShowFactoryPackageDetailResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.ShowPackageDetailRespReleasePackage`
        """
        return self._release_package

    @release_package.setter
    def release_package(self, release_package):
        """Sets the release_package of this ShowFactoryPackageDetailResponse.

        :param release_package: The release_package of this ShowFactoryPackageDetailResponse.
        :type release_package: :class:`huaweicloudsdkdataartsstudio.v1.ShowPackageDetailRespReleasePackage`
        """
        self._release_package = release_package

    @property
    def task_details(self):
        """Gets the task_details of this ShowFactoryPackageDetailResponse.

        发布任务详情

        :return: The task_details of this ShowFactoryPackageDetailResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ShowPackageDetailRespTaskDetails`]
        """
        return self._task_details

    @task_details.setter
    def task_details(self, task_details):
        """Sets the task_details of this ShowFactoryPackageDetailResponse.

        发布任务详情

        :param task_details: The task_details of this ShowFactoryPackageDetailResponse.
        :type task_details: list[:class:`huaweicloudsdkdataartsstudio.v1.ShowPackageDetailRespTaskDetails`]
        """
        self._task_details = task_details

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowFactoryPackageDetailResponse.

        :return: The x_request_id of this ShowFactoryPackageDetailResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowFactoryPackageDetailResponse.

        :param x_request_id: The x_request_id of this ShowFactoryPackageDetailResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowFactoryPackageDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
