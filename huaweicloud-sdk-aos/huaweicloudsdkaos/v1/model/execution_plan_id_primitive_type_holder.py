# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecutionPlanIdPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_plan_id': 'str'
    }

    attribute_map = {
        'execution_plan_id': 'execution_plan_id'
    }

    def __init__(self, execution_plan_id=None):
        """ExecutionPlanIdPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param execution_plan_id: 执行计划（execution_plan）的唯一Id。  此Id由资源编排服务在生成执行计划的时候生成，为UUID。  由于执行计划名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的执行计划，删除，再重新创建一个同名执行计划。  对于团队并行开发，用户可能希望确保，当前我操作的执行计划就是我认为的那个，而不是其他队友删除后创建的同名执行计划。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的执行计划所对应的ID都不相同，更新不会影响ID。如果给予的execution_plan_id和当前执行计划的ID不一致，则返回400  **注意：** * 创建执行计划后，资源编排服务持久化请求并立即返回，客户端不等待请求最终处理完成，用户无法实时感知请求处理结果 * 资源编排服务最终会将异步部署请求排队，在服务端空闲的情况下逐个处理。用户最大等待时长为1小时
        :type execution_plan_id: str
        """
        
        

        self._execution_plan_id = None
        self.discriminator = None

        if execution_plan_id is not None:
            self.execution_plan_id = execution_plan_id

    @property
    def execution_plan_id(self):
        """Gets the execution_plan_id of this ExecutionPlanIdPrimitiveTypeHolder.

        执行计划（execution_plan）的唯一Id。  此Id由资源编排服务在生成执行计划的时候生成，为UUID。  由于执行计划名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的执行计划，删除，再重新创建一个同名执行计划。  对于团队并行开发，用户可能希望确保，当前我操作的执行计划就是我认为的那个，而不是其他队友删除后创建的同名执行计划。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的执行计划所对应的ID都不相同，更新不会影响ID。如果给予的execution_plan_id和当前执行计划的ID不一致，则返回400  **注意：** * 创建执行计划后，资源编排服务持久化请求并立即返回，客户端不等待请求最终处理完成，用户无法实时感知请求处理结果 * 资源编排服务最终会将异步部署请求排队，在服务端空闲的情况下逐个处理。用户最大等待时长为1小时

        :return: The execution_plan_id of this ExecutionPlanIdPrimitiveTypeHolder.
        :rtype: str
        """
        return self._execution_plan_id

    @execution_plan_id.setter
    def execution_plan_id(self, execution_plan_id):
        """Sets the execution_plan_id of this ExecutionPlanIdPrimitiveTypeHolder.

        执行计划（execution_plan）的唯一Id。  此Id由资源编排服务在生成执行计划的时候生成，为UUID。  由于执行计划名仅仅在同一时间下唯一，即用户允许先生成一个叫HelloWorld的执行计划，删除，再重新创建一个同名执行计划。  对于团队并行开发，用户可能希望确保，当前我操作的执行计划就是我认为的那个，而不是其他队友删除后创建的同名执行计划。因此，使用ID就可以做到强匹配。  资源编排服务保证每次创建的执行计划所对应的ID都不相同，更新不会影响ID。如果给予的execution_plan_id和当前执行计划的ID不一致，则返回400  **注意：** * 创建执行计划后，资源编排服务持久化请求并立即返回，客户端不等待请求最终处理完成，用户无法实时感知请求处理结果 * 资源编排服务最终会将异步部署请求排队，在服务端空闲的情况下逐个处理。用户最大等待时长为1小时

        :param execution_plan_id: The execution_plan_id of this ExecutionPlanIdPrimitiveTypeHolder.
        :type execution_plan_id: str
        """
        self._execution_plan_id = execution_plan_id

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
        if not isinstance(other, ExecutionPlanIdPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
