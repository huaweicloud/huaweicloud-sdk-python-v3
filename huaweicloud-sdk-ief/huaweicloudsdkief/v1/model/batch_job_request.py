# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_name': 'str',
        'job_type': 'str',
        'job_content': 'JobContentInfo',
        'description': 'str',
        'tags': 'list[Attributes]'
    }

    attribute_map = {
        'job_name': 'job_name',
        'job_type': 'job_type',
        'job_content': 'job_content',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, job_name=None, job_type=None, job_content=None, description=None, tags=None):
        r"""BatchJobRequest

        The model defined in huaweicloud sdk

        :param job_name: 批量作业名称，允许输入小写字母，数字，中划线，不能以中划线开头或结尾，最大长度为26位
        :type job_name: str
        :param job_type: 批量作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级
        :type job_type: str
        :param job_content: 
        :type job_content: :class:`huaweicloudsdkief.v1.JobContentInfo`
        :param description: 批量作业描述
        :type description: str
        :param tags: 批量作业标签
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        
        

        self._job_name = None
        self._job_type = None
        self._job_content = None
        self._description = None
        self._tags = None
        self.discriminator = None

        self.job_name = job_name
        self.job_type = job_type
        if job_content is not None:
            self.job_content = job_content
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def job_name(self):
        r"""Gets the job_name of this BatchJobRequest.

        批量作业名称，允许输入小写字母，数字，中划线，不能以中划线开头或结尾，最大长度为26位

        :return: The job_name of this BatchJobRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this BatchJobRequest.

        批量作业名称，允许输入小写字母，数字，中划线，不能以中划线开头或结尾，最大长度为26位

        :param job_name: The job_name of this BatchJobRequest.
        :type job_name: str
        """
        self._job_name = job_name

    @property
    def job_type(self):
        r"""Gets the job_type of this BatchJobRequest.

        批量作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级

        :return: The job_type of this BatchJobRequest.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this BatchJobRequest.

        批量作业类型，支持以下选项： - node_upgrade： 节点升级 - deployment_deploy：应用部署 - deployment_upgrade：应用升级

        :param job_type: The job_type of this BatchJobRequest.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def job_content(self):
        r"""Gets the job_content of this BatchJobRequest.

        :return: The job_content of this BatchJobRequest.
        :rtype: :class:`huaweicloudsdkief.v1.JobContentInfo`
        """
        return self._job_content

    @job_content.setter
    def job_content(self, job_content):
        r"""Sets the job_content of this BatchJobRequest.

        :param job_content: The job_content of this BatchJobRequest.
        :type job_content: :class:`huaweicloudsdkief.v1.JobContentInfo`
        """
        self._job_content = job_content

    @property
    def description(self):
        r"""Gets the description of this BatchJobRequest.

        批量作业描述

        :return: The description of this BatchJobRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this BatchJobRequest.

        批量作业描述

        :param description: The description of this BatchJobRequest.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this BatchJobRequest.

        批量作业标签

        :return: The tags of this BatchJobRequest.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchJobRequest.

        批量作业标签

        :param tags: The tags of this BatchJobRequest.
        :type tags: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._tags = tags

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
        if not isinstance(other, BatchJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
