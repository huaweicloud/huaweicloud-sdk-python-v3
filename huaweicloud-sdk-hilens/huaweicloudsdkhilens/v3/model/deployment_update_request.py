# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentUpdateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deployment': 'DeploymentRequest',
        'description': 'str',
        'tags': 'list[DeploymentTag]'
    }

    attribute_map = {
        'deployment': 'deployment',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, deployment=None, description=None, tags=None):
        r"""DeploymentUpdateRequest

        The model defined in huaweicloud sdk

        :param deployment: 
        :type deployment: :class:`huaweicloudsdkhilens.v3.DeploymentRequest`
        :param description: 应用部署描述修改，只修改描述不需要传deployment参数。最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param tags: 部署标签
        :type tags: list[:class:`huaweicloudsdkhilens.v3.DeploymentTag`]
        """
        
        

        self._deployment = None
        self._description = None
        self._tags = None
        self.discriminator = None

        if deployment is not None:
            self.deployment = deployment
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def deployment(self):
        r"""Gets the deployment of this DeploymentUpdateRequest.

        :return: The deployment of this DeploymentUpdateRequest.
        :rtype: :class:`huaweicloudsdkhilens.v3.DeploymentRequest`
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        r"""Sets the deployment of this DeploymentUpdateRequest.

        :param deployment: The deployment of this DeploymentUpdateRequest.
        :type deployment: :class:`huaweicloudsdkhilens.v3.DeploymentRequest`
        """
        self._deployment = deployment

    @property
    def description(self):
        r"""Gets the description of this DeploymentUpdateRequest.

        应用部署描述修改，只修改描述不需要传deployment参数。最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this DeploymentUpdateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DeploymentUpdateRequest.

        应用部署描述修改，只修改描述不需要传deployment参数。最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this DeploymentUpdateRequest.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        r"""Gets the tags of this DeploymentUpdateRequest.

        部署标签

        :return: The tags of this DeploymentUpdateRequest.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.DeploymentTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this DeploymentUpdateRequest.

        部署标签

        :param tags: The tags of this DeploymentUpdateRequest.
        :type tags: list[:class:`huaweicloudsdkhilens.v3.DeploymentTag`]
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
        if not isinstance(other, DeploymentUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
