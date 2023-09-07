# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteStackEnhancedRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stack_id': 'str',
        'retain_all_resources': 'bool'
    }

    attribute_map = {
        'stack_id': 'stack_id',
        'retain_all_resources': 'retain_all_resources'
    }

    def __init__(self, stack_id=None, retain_all_resources=None):
        """DeleteStackEnhancedRequestBody

        The model defined in huaweicloud sdk

        :param stack_id: 资源栈（stack）的唯一Id。  此Id由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400
        :type stack_id: str
        :param retain_all_resources: 删除资源栈是否保留资源的标志位，如果不传默认为false，即默认不保留资源（删除资源栈后会删除资源栈中的资源）  * DeleteStackEnhanced API中，若该参数未在RequestBody中给予，则删除时不会保留资源栈中的资源*
        :type retain_all_resources: bool
        """
        
        

        self._stack_id = None
        self._retain_all_resources = None
        self.discriminator = None

        if stack_id is not None:
            self.stack_id = stack_id
        if retain_all_resources is not None:
            self.retain_all_resources = retain_all_resources

    @property
    def stack_id(self):
        """Gets the stack_id of this DeleteStackEnhancedRequestBody.

        资源栈（stack）的唯一Id。  此Id由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400

        :return: The stack_id of this DeleteStackEnhancedRequestBody.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        """Sets the stack_id of this DeleteStackEnhancedRequestBody.

        资源栈（stack）的唯一Id。  此Id由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给与的stack_id和当前资源栈的ID不一致，则返回400

        :param stack_id: The stack_id of this DeleteStackEnhancedRequestBody.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def retain_all_resources(self):
        """Gets the retain_all_resources of this DeleteStackEnhancedRequestBody.

        删除资源栈是否保留资源的标志位，如果不传默认为false，即默认不保留资源（删除资源栈后会删除资源栈中的资源）  * DeleteStackEnhanced API中，若该参数未在RequestBody中给予，则删除时不会保留资源栈中的资源*

        :return: The retain_all_resources of this DeleteStackEnhancedRequestBody.
        :rtype: bool
        """
        return self._retain_all_resources

    @retain_all_resources.setter
    def retain_all_resources(self, retain_all_resources):
        """Sets the retain_all_resources of this DeleteStackEnhancedRequestBody.

        删除资源栈是否保留资源的标志位，如果不传默认为false，即默认不保留资源（删除资源栈后会删除资源栈中的资源）  * DeleteStackEnhanced API中，若该参数未在RequestBody中给予，则删除时不会保留资源栈中的资源*

        :param retain_all_resources: The retain_all_resources of this DeleteStackEnhancedRequestBody.
        :type retain_all_resources: bool
        """
        self._retain_all_resources = retain_all_resources

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
        if not isinstance(other, DeleteStackEnhancedRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
