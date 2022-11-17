# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FGSDeploymentJobsParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_id': 'str',
        'handler': 'str'
    }

    attribute_map = {
        'file_id': 'file_id',
        'handler': 'handler'
    }

    def __init__(self, file_id=None, handler=None):
        """FGSDeploymentJobsParam

        The model defined in huaweicloud sdk

        :param file_id: 版本包id,使用历史版本包部署时需要
        :type file_id: str
        :param handler: 函数入口
        :type handler: str
        """
        
        

        self._file_id = None
        self._handler = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if handler is not None:
            self.handler = handler

    @property
    def file_id(self):
        """Gets the file_id of this FGSDeploymentJobsParam.

        版本包id,使用历史版本包部署时需要

        :return: The file_id of this FGSDeploymentJobsParam.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this FGSDeploymentJobsParam.

        版本包id,使用历史版本包部署时需要

        :param file_id: The file_id of this FGSDeploymentJobsParam.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def handler(self):
        """Gets the handler of this FGSDeploymentJobsParam.

        函数入口

        :return: The handler of this FGSDeploymentJobsParam.
        :rtype: str
        """
        return self._handler

    @handler.setter
    def handler(self, handler):
        """Sets the handler of this FGSDeploymentJobsParam.

        函数入口

        :param handler: The handler of this FGSDeploymentJobsParam.
        :type handler: str
        """
        self._handler = handler

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
        if not isinstance(other, FGSDeploymentJobsParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
