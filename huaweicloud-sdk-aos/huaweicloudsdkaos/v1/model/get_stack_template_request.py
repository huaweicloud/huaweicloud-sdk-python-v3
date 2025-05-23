# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetStackTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_request_id': 'str',
        'stack_name': 'str',
        'stack_id': 'str',
        'access_control_source_ips': 'list[str]',
        'access_control_source_vpc_ids': 'list[str]'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'stack_name': 'stack_name',
        'stack_id': 'stack_id',
        'access_control_source_ips': 'access_control_source_ips',
        'access_control_source_vpc_ids': 'access_control_source_vpc_ids'
    }

    def __init__(self, client_request_id=None, stack_name=None, stack_id=None, access_control_source_ips=None, access_control_source_vpc_ids=None):
        r"""GetStackTemplateRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param stack_name: 资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_name: str
        :param stack_id: 资源栈（stack）的唯一Id。  此Id由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给予的stack_id和当前资源栈的ID不一致，则返回400
        :type stack_id: str
        :param access_control_source_ips: 允许访问资源栈模板的source ip列表，source ip应是具有CIDR表示法且带有子网掩码的IPv4地址。
        :type access_control_source_ips: list[str]
        :param access_control_source_vpc_ids: 允许访问资源栈模板的source vpc id列表， source vpc id应仅包含小写字母、数字或中划线。
        :type access_control_source_vpc_ids: list[str]
        """
        
        

        self._client_request_id = None
        self._stack_name = None
        self._stack_id = None
        self._access_control_source_ips = None
        self._access_control_source_vpc_ids = None
        self.discriminator = None

        self.client_request_id = client_request_id
        self.stack_name = stack_name
        if stack_id is not None:
            self.stack_id = stack_id
        if access_control_source_ips is not None:
            self.access_control_source_ips = access_control_source_ips
        if access_control_source_vpc_ids is not None:
            self.access_control_source_vpc_ids = access_control_source_vpc_ids

    @property
    def client_request_id(self):
        r"""Gets the client_request_id of this GetStackTemplateRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this GetStackTemplateRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        r"""Sets the client_request_id of this GetStackTemplateRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this GetStackTemplateRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def stack_name(self):
        r"""Gets the stack_name of this GetStackTemplateRequest.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_name of this GetStackTemplateRequest.
        :rtype: str
        """
        return self._stack_name

    @stack_name.setter
    def stack_name(self, stack_name):
        r"""Sets the stack_name of this GetStackTemplateRequest.

        资源栈的名称。此名字在domain_id+区域+project_id下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_name: The stack_name of this GetStackTemplateRequest.
        :type stack_name: str
        """
        self._stack_name = stack_name

    @property
    def stack_id(self):
        r"""Gets the stack_id of this GetStackTemplateRequest.

        资源栈（stack）的唯一Id。  此Id由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给予的stack_id和当前资源栈的ID不一致，则返回400

        :return: The stack_id of this GetStackTemplateRequest.
        :rtype: str
        """
        return self._stack_id

    @stack_id.setter
    def stack_id(self, stack_id):
        r"""Sets the stack_id of this GetStackTemplateRequest.

        资源栈（stack）的唯一Id。  此Id由资源编排服务在生成资源栈的时候生成，为UUID。  由于资源栈名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈，删除，再重新创建一个同名资源栈。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈就是我认为的那个，而不是其他队友删除后创建的同名资源栈。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈所对应的ID都不相同，更新不会影响ID。如果给予的stack_id和当前资源栈的ID不一致，则返回400

        :param stack_id: The stack_id of this GetStackTemplateRequest.
        :type stack_id: str
        """
        self._stack_id = stack_id

    @property
    def access_control_source_ips(self):
        r"""Gets the access_control_source_ips of this GetStackTemplateRequest.

        允许访问资源栈模板的source ip列表，source ip应是具有CIDR表示法且带有子网掩码的IPv4地址。

        :return: The access_control_source_ips of this GetStackTemplateRequest.
        :rtype: list[str]
        """
        return self._access_control_source_ips

    @access_control_source_ips.setter
    def access_control_source_ips(self, access_control_source_ips):
        r"""Sets the access_control_source_ips of this GetStackTemplateRequest.

        允许访问资源栈模板的source ip列表，source ip应是具有CIDR表示法且带有子网掩码的IPv4地址。

        :param access_control_source_ips: The access_control_source_ips of this GetStackTemplateRequest.
        :type access_control_source_ips: list[str]
        """
        self._access_control_source_ips = access_control_source_ips

    @property
    def access_control_source_vpc_ids(self):
        r"""Gets the access_control_source_vpc_ids of this GetStackTemplateRequest.

        允许访问资源栈模板的source vpc id列表， source vpc id应仅包含小写字母、数字或中划线。

        :return: The access_control_source_vpc_ids of this GetStackTemplateRequest.
        :rtype: list[str]
        """
        return self._access_control_source_vpc_ids

    @access_control_source_vpc_ids.setter
    def access_control_source_vpc_ids(self, access_control_source_vpc_ids):
        r"""Sets the access_control_source_vpc_ids of this GetStackTemplateRequest.

        允许访问资源栈模板的source vpc id列表， source vpc id应仅包含小写字母、数字或中划线。

        :param access_control_source_vpc_ids: The access_control_source_vpc_ids of this GetStackTemplateRequest.
        :type access_control_source_vpc_ids: list[str]
        """
        self._access_control_source_vpc_ids = access_control_source_vpc_ids

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
        if not isinstance(other, GetStackTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
