# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStackInstanceRequest:

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
        'stack_set_name': 'str',
        'stack_instance_addr': 'str',
        'stack_set_id': 'str',
        'call_identity': 'str'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'stack_set_name': 'stack_set_name',
        'stack_instance_addr': 'stack_instance_addr',
        'stack_set_id': 'stack_set_id',
        'call_identity': 'call_identity'
    }

    def __init__(self, client_request_id=None, stack_set_name=None, stack_instance_addr=None, stack_set_id=None, call_identity=None):
        r"""ShowStackInstanceRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param stack_set_name: 资源栈集的名称。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。
        :type stack_set_name: str
        :param stack_instance_addr: 资源栈实例的唯一地址。该地址由region和stack_domain_id通过\&quot;/\&quot;（转义后为%2f或%2F）拼接而成。该地址在domain_id+region+stack_set_name下唯一。
        :type stack_instance_addr: str
        :param stack_set_id: 资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我认为的那个，而不是其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400
        :type stack_set_id: str
        :param call_identity: 仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 * 无论指定何种用户身份，创建或部署的资源栈集始终在组织管理账号名下。*   * &#x60;SELF&#x60; - 以组织管理账号身份调用。   * &#x60;DELEGATED_ADMIN&#x60; - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。
        :type call_identity: str
        """
        
        

        self._client_request_id = None
        self._stack_set_name = None
        self._stack_instance_addr = None
        self._stack_set_id = None
        self._call_identity = None
        self.discriminator = None

        self.client_request_id = client_request_id
        self.stack_set_name = stack_set_name
        self.stack_instance_addr = stack_instance_addr
        if stack_set_id is not None:
            self.stack_set_id = stack_set_id
        if call_identity is not None:
            self.call_identity = call_identity

    @property
    def client_request_id(self):
        r"""Gets the client_request_id of this ShowStackInstanceRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this ShowStackInstanceRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        r"""Sets the client_request_id of this ShowStackInstanceRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this ShowStackInstanceRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def stack_set_name(self):
        r"""Gets the stack_set_name of this ShowStackInstanceRequest.

        资源栈集的名称。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :return: The stack_set_name of this ShowStackInstanceRequest.
        :rtype: str
        """
        return self._stack_set_name

    @stack_set_name.setter
    def stack_set_name(self, stack_set_name):
        r"""Sets the stack_set_name of this ShowStackInstanceRequest.

        资源栈集的名称。此名字在domain_id+region下应唯一，可以使用中文、大小写英文、数字、下划线、中划线。首字符需为中文或者英文，区分大小写。

        :param stack_set_name: The stack_set_name of this ShowStackInstanceRequest.
        :type stack_set_name: str
        """
        self._stack_set_name = stack_set_name

    @property
    def stack_instance_addr(self):
        r"""Gets the stack_instance_addr of this ShowStackInstanceRequest.

        资源栈实例的唯一地址。该地址由region和stack_domain_id通过\"/\"（转义后为%2f或%2F）拼接而成。该地址在domain_id+region+stack_set_name下唯一。

        :return: The stack_instance_addr of this ShowStackInstanceRequest.
        :rtype: str
        """
        return self._stack_instance_addr

    @stack_instance_addr.setter
    def stack_instance_addr(self, stack_instance_addr):
        r"""Sets the stack_instance_addr of this ShowStackInstanceRequest.

        资源栈实例的唯一地址。该地址由region和stack_domain_id通过\"/\"（转义后为%2f或%2F）拼接而成。该地址在domain_id+region+stack_set_name下唯一。

        :param stack_instance_addr: The stack_instance_addr of this ShowStackInstanceRequest.
        :type stack_instance_addr: str
        """
        self._stack_instance_addr = stack_instance_addr

    @property
    def stack_set_id(self):
        r"""Gets the stack_set_id of this ShowStackInstanceRequest.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我认为的那个，而不是其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :return: The stack_set_id of this ShowStackInstanceRequest.
        :rtype: str
        """
        return self._stack_set_id

    @stack_set_id.setter
    def stack_set_id(self, stack_set_id):
        r"""Sets the stack_set_id of this ShowStackInstanceRequest.

        资源栈集（stack_set）的唯一ID。  此ID由资源编排服务在生成资源栈集的时候生成，为UUID。  由于资源栈集名称仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的资源栈集，删除，再重新创建一个同名资源栈集。  对于团队并行开发，用户可能希望确保，当前我操作的资源栈集就是我认为的那个，而不是其他队友删除后创建的同名资源栈集。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的资源栈集所对应的ID都不相同，更新不会影响ID。如果给予的stack_set_id和当前资源栈集的ID不一致，则返回400

        :param stack_set_id: The stack_set_id of this ShowStackInstanceRequest.
        :type stack_set_id: str
        """
        self._stack_set_id = stack_set_id

    @property
    def call_identity(self):
        r"""Gets the call_identity of this ShowStackInstanceRequest.

        仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 * 无论指定何种用户身份，创建或部署的资源栈集始终在组织管理账号名下。*   * `SELF` - 以组织管理账号身份调用。   * `DELEGATED_ADMIN` - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。

        :return: The call_identity of this ShowStackInstanceRequest.
        :rtype: str
        """
        return self._call_identity

    @call_identity.setter
    def call_identity(self, call_identity):
        r"""Sets the call_identity of this ShowStackInstanceRequest.

        仅支持资源栈集权限模式为SERVICE_MANAGED时指定该参数。用于指定用户是以组织管理账号还是成员账号中的服务委托管理员身份调用资源栈集。默认为SELF。 * 无论指定何种用户身份，创建或部署的资源栈集始终在组织管理账号名下。*   * `SELF` - 以组织管理账号身份调用。   * `DELEGATED_ADMIN` - 以服务委托管理员身份调用。用户的华为云账号必须在组织中已经被注册为”资源编排资源栈集服务“的委托管理员。

        :param call_identity: The call_identity of this ShowStackInstanceRequest.
        :type call_identity: str
        """
        self._call_identity = call_identity

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
        if not isinstance(other, ShowStackInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
